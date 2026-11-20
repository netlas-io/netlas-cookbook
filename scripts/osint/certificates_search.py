import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('certificate.subject.street_address:*')

for item in results.get("items", []):
    data = item["data"]
    print(data["uri"])
    print((data.get("certificate") or {}).get("subject"))
