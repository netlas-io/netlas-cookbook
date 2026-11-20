import os

import requests

api_key = os.environ.get("NETLAS_API_KEY")
if not api_key:
    raise SystemExit("Set NETLAS_API_KEY to your Netlas API key.")

response = requests.get(
    "https://app.netlas.io/api/domains/",
    params={"q": "domain:netlas.io"},
    headers={"Authorization": f"Bearer {api_key}"},
    timeout=30,
)
response.raise_for_status()

print(response.json())
