import os

import netlas
from bs4 import BeautifulSoup

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
results = netlas_connection.search('host:example.com AND http.body:*')

for item in results.get("items", []):
    data = item["data"]
    print(data["uri"])
    body = (data.get("http") or {}).get("body") or ""
    soup = BeautifulSoup(body, "html.parser")
    for heading in soup.find_all("h1"):
        print(heading.get_text(" ", strip=True))
