import os

import netlas

api_key = os.environ.get("NETLAS_API_KEY")
if not api_key:
    raise SystemExit("Set NETLAS_API_KEY to your Netlas API key.")

connection = netlas.Netlas(api_key=api_key)
results = connection.search(query="host:netlas.io")

for item in results["items"]:
    uri = item.get("data", {}).get("uri")
    if uri:
        print(uri)
