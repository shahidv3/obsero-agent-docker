import requests

def query_prometheus(prom_url, query):
    try:
        resp = requests.get(f"{prom_url}/api/v1/query", params={"query": query})
        data = resp.json()
        if data["status"] == "success":
            return data["data"]["result"]
        return []
    except Exception as e:
        print(f"Error querying Prometheus: {e}")
        return []
