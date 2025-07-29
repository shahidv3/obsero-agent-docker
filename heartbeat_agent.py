import os
import time
import requests

CLUSTER_ID = os.getenv("CLUSTER_ID", "unknown")
OBSERO_API_URL = os.getenv("OBSERO_API_URL", "http://localhost:8000")
HEARTBEAT_INTERVAL = int(os.getenv("HEARTBEAT_INTERVAL", 60))

print(f"using API url : {OBSERO_API_URL}")
print(f"Cluster ID: {CLUSTER_ID}")
print(f"interval: {HEARTBEAT_INTERVAL}")

def run_heartbeat():
    url = f"{OBSERO_API_URL}/agents/heartbeat"
    payload = {
        "cluster_id": CLUSTER_ID,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    try:
        response = requests.post(url, json=payload, timeout=5)
        print(f"✅ Sent heartbeat: {response.status_code} {response.text}")
    except Exception as e:
        print(f"❌ Failed to send heartbeat: {e}")

if __name__ == "__main__":
    print(f"🚀 Starting heartbeat agent for cluster: {CLUSTER_ID}")
    while True:
        run_heartbeat()
        time.sleep(HEARTBEAT_INTERVAL)

    