import os
import re

import netlas

netlas_connection = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
email_pattern = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
results = netlas_connection.search('host:example.com AND http.body:*')

for item in results.get("items", []):
    data = item["data"]
    print(data["uri"])
    body = (data.get("http") or {}).get("body") or ""
    for email in email_pattern.findall(body):
        print(email)
