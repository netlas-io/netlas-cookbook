import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('(http.title:alla OR http.body:alla) AND http.body:mp3')

for item in results.get("items", []):
    data = item["data"]
    print(data["ip"])
    print(data["uri"])
    print((data.get("http") or {}).get("title"))
