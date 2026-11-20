import os
import re
from pathlib import Path

import netlas


client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
with Path(__file__).with_name("domains.txt").open(encoding="utf-8") as domain_file:
    for line_number, line in enumerate(domain_file, start=1):
        domain = line.strip().lower().rstrip(".")
        if not domain or domain.startswith("#"):
            continue
        if not re.fullmatch(r"[a-z0-9-]+(?:\.[a-z0-9-]+)+", domain):
            raise SystemExit(f"Invalid hostname in domains.txt on line {line_number}: {line.strip()}")
        result = client.search(
            query=f'domain:"{domain}"', datatype="whois-domain", fields="domain,registrar.name"
        )
        for item in result.get("items", []):
            data = item["data"]
            print(data["domain"], (data.get("registrar") or {}).get("name", ""))
