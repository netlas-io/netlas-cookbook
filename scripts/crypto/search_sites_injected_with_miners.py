import os

import netlas

api_key = os.getenv("NETLAS_API_KEY")
if not api_key:
    raise SystemExit("Set NETLAS_API_KEY to your Netlas API key.")

connection = netlas.Netlas(api_key=api_key)
query = 'host:(example.com OR *.example.com) AND http.body:coinhive'
results = connection.search(query=query, fields="uri")

for item in results["items"]:
    print(item["data"]["uri"])
