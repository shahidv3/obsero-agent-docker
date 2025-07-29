FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY runner.py .
COPY heartbeat_agent.py .
#COPY metrics_plugin.py .
#COPY prometheus_queries.yaml .


# Default heartbeat interval (can be overridden by args/env)
ENV HEARTBEAT_INTERVAL=60
ENV METRICS_INTERVAL=60

# Run the heartbeat agent
CMD ["python", "heartbeat_agent.py"]
