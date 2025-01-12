import boto3
from prometheus_client import start_http_server, Gauge
import time

# Initialize a CloudWatch client using boto3
cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')  # Change the region as needed

# Prometheus metric for CloudWatch Alarms
alarm_metric = Gauge('cloudwatch_alarm_status', 'Status of CloudWatch Alarms',
                     ['alarm_name', 'state', 'region'])

def fetch_alarms():
    """
    Fetch the CloudWatch alarms and return them.
    This will fetch all CloudWatch alarms for the region defined in the boto3 client.
    """
    alarms = []
    response = cloudwatch.describe_alarms(StateValue='ALARM')  # Get only alarms in ALARM state
    alarms.extend(response['MetricAlarms'])

    # Paginate through all alarms if needed
    while 'NextToken' in response:
        response = cloudwatch.describe_alarms(StateValue='ALARM', NextToken=response['NextToken'])
        alarms.extend(response['MetricAlarms'])

    return alarms

def export_alarms():
    """
    Export CloudWatch alarm data to Prometheus format.
    """
    alarms = fetch_alarms()

    for alarm in alarms:
        alarm_name = alarm['AlarmName']
        state = alarm['StateValue']  # ALARM, OK, or INSUFFICIENT_DATA
        region = cloudwatch.meta.region_name

        # Set the alarm state in the Prometheus metric
        alarm_metric.labels(alarm_name=alarm_name, state=state, region=region).set(1 if state == 'ALARM' else 0)

def main():
    # Start a Prometheus-compatible HTTP server
    start_http_server(8000)  # Expose metrics at localhost:8000
    
    print("Starting CloudWatch Alarm Exporter...")
    
    # Export alarm data every 60 seconds
    while True:
        export_alarms()
        time.sleep(60)

if __name__ == "__main__":
    main()
