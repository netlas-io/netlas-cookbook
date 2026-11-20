import os

import netlas

api_key = os.getenv("NETLAS_API_KEY")
if not api_key:
    raise SystemExit("Set NETLAS_API_KEY to your Netlas API key.")

connection = netlas.Netlas(api_key=api_key)
query = 'ip:"192.0.2.0/24" AND http.headers.www_authenticate:antminer'
results = connection.search(query=query, fields="uri,http.headers.www_authenticate")

for item in results["items"]:
    data = item["data"]
    headers = ((data.get("http") or {}).get("headers") or {})
    print(data["uri"], headers.get("www_authenticate", ""), sep="\t")
