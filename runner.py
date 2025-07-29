import os
from heartbeat_agent import run_heartbeat
from metrics_plugin import run_metrics

if __name__ == "__main__":
    print("🚀 Starting Obsero Agent")
    run_heartbeat()

    if os.getenv("METRICS_ENABLED", "true").lower() == "true":
        run_metrics()

