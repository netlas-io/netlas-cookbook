import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('ftp.banner:"pure-ftpd"')

for item in results.get("items", []):
    data = item["data"]
    print(data["ip"])
    print(data["uri"])
    print((data.get("ftp") or {}).get("banner"))
