import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('http.body:(2025550142 OR "202 555 0142")')

for item in results.get("items", []):
    data = item["data"]
    print(data["ip"])
    print(data["uri"])
