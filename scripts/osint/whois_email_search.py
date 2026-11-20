import os

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('whois.related_nets.contacts.emails:"hostmaster@example.com"')

for item in results.get("items", []):
    data = item["data"]
    print(data["uri"])
    print((data.get("geo") or {}).get("country"))
    print((data.get("whois") or {}).get("related_nets", []))
