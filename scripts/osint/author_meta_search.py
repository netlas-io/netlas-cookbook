import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('http.meta:nazar')

for item in results.get("items", []):
    data = item["data"]
    print(data["uri"])
    http = data.get("http") or {}
    print(http.get("title"))
    print(http.get("meta"))
