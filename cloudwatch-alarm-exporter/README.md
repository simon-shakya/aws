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
