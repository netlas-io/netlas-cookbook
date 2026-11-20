import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('prot7:http AND host:(example.com OR *.example.com) AND contacts.address:*')

for item in results.get("items", []):
    data = item["data"]
    print(data["uri"])
    print((data.get("contacts") or {}).get("address"))
