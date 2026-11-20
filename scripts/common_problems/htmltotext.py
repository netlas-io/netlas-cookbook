import os

import html2text
import netlas


client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
result = client.search(query="host:example.com AND http.body:*", fields="uri,http.body")
for item in result.get("items", []):
    data = item["data"]
    body = (data.get("http") or {}).get("body")
    if body:
        print(data.get("uri", ""))
        print(html2text.html2text(body))
