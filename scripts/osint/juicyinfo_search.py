import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('host:(example.com OR *.example.com) AND http.body:pdf')

for item in results.get("items", []):
    data = item["data"]
    print(data["uri"])
    print((data.get("http") or {}).get("body", ""))
