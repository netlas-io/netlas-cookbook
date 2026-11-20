import argparse
import os
from ipaddress import IPv4Network

import netlas


parser = argparse.ArgumentParser(description="Find indexed DNS A records in a subnet.")
parser.add_argument("subnet", type=IPv4Network, help="IPv4 subnet in CIDR notation")
args = parser.parse_args()

client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
result = client.search(query=f'a:"{args.subnet}"', datatype="domain", fields="domain")
for item in result.get("items", []):
    print(item["data"]["domain"])
