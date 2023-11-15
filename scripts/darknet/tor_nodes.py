import netlas
import urllib
import time

apikey = 'YOUR_API_KEY'

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# read file with Tor Exit Nodes IPs line by line
response = urllib.request.urlopen('https://check.torproject.org/torbulkexitlist?ip=1.1.1.1')
ip_lines = response.readlines()

# save each line to ip variable
for ip in ip_lines:
     # wait one second
     time.sleep(1)
     # conver byte string to text
     ip=ip.decode("utf-8")
     # retrieve data from responses by query `ip: + tor exit node ip`
     netlas_query = netlas_connection.query(query="ip:"+ip)

    # iterate over data and print: ip, geo data, banner text

     for response in netlas_query['items']:
         print(response['data']['ip'])
         print(response['data']['geo'])
         print(response['data']['ntp']['banner'])
     pass
pass