# CloudWatch Alarm Exporter

This is a simple exporter to collect and expose AWS CloudWatch alarm states as Prometheus metrics.

## Requirements

- Python 3.x
- AWS credentials configured (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or via IAM role/`~/.aws/credentials`)
- Prometheus (for scraping metrics)

## Install Dependencies

First, clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/cloudwatch-alarm-exporter.git
cd cloudwatch-alarm-exporter
pip install -r requirements.txt
```

## Configuration
This exporter uses the boto3 library to interact with AWS CloudWatch. Make sure your AWS credentials are configured properly (e.g., via ~/.aws/credentials or environment variables).

You can specify the AWS region in the script (cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')).

## Running the Exporter
To start the exporter:

```bash
python cloudwatch_alarm_exporter.py
```

The exporter will start exposing metrics at http://localhost:8000/metrics, where Prometheus can scrape them.

## Prometheus Configuration
Add the following scrape job to your prometheus.yml configuration:

```bash
scrape_configs:
  - job_name: 'cloudwatch_alarms'
    static_configs:
      - targets: ['localhost:8000']
```
How to setup Prometheus in detail steps defined here

## Additional Information

```

### 5. **Push to GitHub**

1. Initialize your Git repository:
 
    git init


2. Add your GitHub repository as the remote:
   
    git remote add origin https://github.com/yourusername/cloudwatch-alarm-exporter.git
    

3. Add, commit, and push the files:

    git add .
    git commit -m "Initial commit of CloudWatch Alarm Exporter"
    git push -u origin master
   

---

### Final Steps

Once you have completed these steps and pushed the code to GitHub, you can:

1. Access your repository via GitHub.
2. Share the repository link with others, or use it to deploy the exporter on your servers.
3. Set up Prometheus to scrape metrics from the exporter as described in the `README.md`.

---

Let me know if you need help with any of the steps or further guidance on deployment!


