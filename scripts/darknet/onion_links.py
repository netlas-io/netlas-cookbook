import os
import re

import netlas


onion_address = re.compile(
    r"(?<![a-z0-9-])[a-z2-7]{56}\.onion(?![a-z0-9-]|\.[a-z0-9-])",
    re.IGNORECASE | re.ASCII,
)
client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
result = client.search(query="http.body:onion", fields="uri,http.body")
for item in result.get("items", []):
    data = item["data"]
    body = (data.get("http") or {}).get("body") or ""
    for address in sorted({value.lower() for value in onion_address.findall(body)}):
        print(data.get("uri", ""), address)
