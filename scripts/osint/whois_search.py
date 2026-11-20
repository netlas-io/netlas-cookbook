import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('domain:github.com', datatype='whois-domain')

for item in results.get("items", []):
    data = item["data"]
    print(data["domain"])
    print((data.get("registrant") or {}).get("organization"))
