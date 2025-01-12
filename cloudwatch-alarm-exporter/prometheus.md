# Prometheus setup Locally

To set up Prometheus locally using Docker, follow these steps. Prometheus is a powerful open-source system monitoring and alerting toolkit that is commonly used to collect and query metrics. Running Prometheus in Docker simplifies the setup and ensures you have an isolated environment.

## Step 1: Install Docker
If you don't have Docker installed, you can install it from Docker's official site. Follow the instructions for your operating system.

## Step 2: Create a Prometheus Configuration File
Prometheus uses a configuration file (prometheus.yml) to define how it collects metrics. For this example, we'll use the default configuration.

Create a directory for Prometheus:

```bash
mkdir prometheus
cd prometheus
```

Inside the directory, create a prometheus.yml file with the following content:

```bash

global:
  scrape_interval: 15s  # Default scrape interval

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
```
This configuration tells Prometheus to scrape its own metrics every 15 seconds.

## Step 3: Run Prometheus with Docker
Now, let's run Prometheus using Docker. In the prometheus directory, run the following command:

```bash

docker run -d \
  --name=prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```
Here's what each option means:

-d: Runs Prometheus in detached mode (in the background).
--name=prometheus: Names the Docker container "prometheus".
-p 9090:9090: Maps the container's port 9090 to your local port 9090 (Prometheus web UI).
-v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml: Mounts your prometheus.yml config file into the container.

## Step 4: Access Prometheus Web UI
Go to the "Targets" tab in the Prometheus web UI (http://localhost:9090/targets).


Step 5: Verify Prometheus is Scraping Metrics

You should see the target localhost:9090 listed under the "prometheus" job, which indicates that Prometheus is scraping its own metrics.

## Step 6: Stop the Prometheus Docker Container
If you want to stop the Prometheus container, you can run:

```bash

docker stop prometheus
```
If you want to remove the container, use:

```bash

docker rm prometheus
```
## Step 7: (Optional) Run Prometheus with Docker Compose
You can also use Docker Compose to manage Prometheus along with other services (like exporters). Here's how to run Prometheus using Docker Compose:

Create a docker-compose.yml file in the prometheus directory:

```bash
yaml
Copy code
version: '3'
services:
  prometheus:
    image: prom/prometheus
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    restart: always
```
Run Docker Compose:

```bash

docker-compose up -d
Access Prometheus at http://localhost:9090.
```

## Step 8: Adding Exporters
To collect metrics from other services (e.g., Node Exporter for system metrics), you can modify the prometheus.yml configuration and set up additional exporters.

For example, to scrape system metrics using the Node Exporter:

Add Node Exporter to your prometheus.yml:

```bash
yaml
Copy code
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node_exporter'
    static_configs:
      - targets: ['localhost:9100']
```
Run the Node Exporter Docker container:

```bash

docker run -d \
  --name=node_exporter \
  -p 9100:9100 \
  prom/node-exporter
```
Now, Prometheus will start scraping Node Exporter metrics from localhost:9100.

Conclusion
You now have a basic Prometheus setup running locally in Docker! You can start collecting and analyzing system or application metrics by configuring Prometheus to scrape various endpoints and setting up different exporters. 
This setup can be extended to monitor various services and integrated with other tools like Grafana for enhanced visualizations.



