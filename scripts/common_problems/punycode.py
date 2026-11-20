import os

import idna
import netlas


suffix = idna.encode("中国").decode("ascii")
client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
result = client.search(query=f"domain:*.{suffix}", datatype="domain", fields="domain")
for item in result.get("items", []):
    domain = item["data"]["domain"]
    try:
        print(idna.decode(domain))
    except idna.IDNAError:
        print(domain)
