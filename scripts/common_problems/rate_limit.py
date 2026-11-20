import os

import netlas


client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
try:
    result = client.search(query="host:example.com", fields="uri", retry=2)
except netlas.ThrottlingError as error:
    raise SystemExit(f"Netlas is still throttling requests. Retry in {error.retry_after} seconds.")

for item in result.get("items", []):
    print(item["data"]["uri"])
