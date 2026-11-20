import os

import netlas


client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
result = client.search(query="smtp.banner:postfix", fields="smtp.banner,uri,isp")
for item in result.get("items", []):
    data = item["data"]
    print(data.get("uri", ""), data.get("isp", ""), (data.get("smtp") or {}).get("banner", ""))
