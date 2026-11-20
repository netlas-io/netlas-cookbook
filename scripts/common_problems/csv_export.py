import csv
import os

import netlas


def spreadsheet_text(value):
    text = "" if value is None else str(value)
    if text.startswith(("\t", "\r", "\n")) or text.lstrip().startswith(("=", "+", "-", "@", "＝", "＋", "－", "＠")):
        return "'" + text
    return text


client = netlas.Netlas(api_key=os.environ["NETLAS_API_KEY"])
result = client.search(query="host:example.com", fields="ip,uri,http.title")

with open("netlas_results.csv", "w", encoding="utf-8", newline="") as output:
    writer = csv.writer(output)
    writer.writerow(["IP", "URL", "Title"])
    for item in result.get("items", []):
        data = item["data"]
        row = (data.get("ip"), data.get("uri"), (data.get("http") or {}).get("title"))
        writer.writerow([spreadsheet_text(value) for value in row])
