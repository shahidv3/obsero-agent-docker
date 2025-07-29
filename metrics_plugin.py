import os
import yaml
import time
import requests
from utils.prometheus import query_prometheus

CLUSTER_ID = os.getenv("CLUSTER_ID")
API_URL = os.getenv("OBSERO_API_URL", "http://localhost:8000")
PROM_URL = os.getenv("PROMETHEUS_URL", "http://localhost:9090")
INTERVAL = int(os.getenv("METRICS_INTERVAL", "60"))

def load_queries():
    with open("prometheus_queries.yaml", "r") as f:
        return yaml.safe_load(f)["queries"]

def run_metrics():
    print(f"📊 Starting metrics plugin for cluster: {CLUSTER_ID}")
    queries = load_queries()
    while True:
        metrics = []
        for query in queries:
            result = query_prometheus(PROM_URL, query["expr"])
            metrics.append({
                "name": query["name"],
                "expr": query["expr"],
                "value": result
            })

        try:
            response = requests.post(
                f"{API_URL}/metrics/ingest",
                json={"cluster_id": CLUSTER_ID, "metrics": metrics},
                timeout=10
            )
            print(f"📤 Sent metrics: {response.status_code}")
        except Exception as e:
            print(f"❌ Failed to send metrics: {e}")

        time.sleep(INTERVAL)
