import argparse
import os
from ipaddress import ip_address
from itertools import islice
from urllib.request import urlopen

import netlas


parser = argparse.ArgumentParser(description="Look up observed Tor exit IPs in Netlas.")
parser.add_argument("--limit", type=int, default=10, help="maximum IPs to look up (default: 10)")
args = parser.parse_args()
if args.limit < 1:
    parser.error("--limit must be positive")

client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
with urlopen("https://check.torproject.org/torbulkexitlist", timeout=15) as feed:
    addresses = (ip_address(line.decode("ascii").strip()) for line in feed if line.strip())
    for address in islice(addresses, args.limit):
        result = client.search(query=f'ip:"{address}"', fields="uri,geo.country")
        for item in result.get("items", []):
            data = item["data"]
            print(address, data.get("uri", ""), (data.get("geo") or {}).get("country", ""))
