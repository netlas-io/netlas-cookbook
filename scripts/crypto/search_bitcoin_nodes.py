import os

import netlas

api_key = os.getenv("NETLAS_API_KEY")
if not api_key:
    raise SystemExit("Set NETLAS_API_KEY to your Netlas API key.")

connection = netlas.Netlas(api_key=api_key)
query = 'ip:"192.0.2.0/24" AND prot4:tcp AND port:8333'
results = connection.search(query=query, fields="uri")

for item in results["items"]:
    print(item["data"]["uri"])
