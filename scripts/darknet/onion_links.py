import netlas
import re

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `http.body:*.onion AND forum`
netlas_query = netlas_connection.query(query="http.body:(*.onion AND forum)")


# iterate over data and print: URL, .onion link from body
for response in netlas_query['items']:
    print(response['data']['uri'])
    onion_links = re.findall("[a-z-1-9]*\.onion", response['data']['http']['body'])  
    try:
         print(onion_links)
    except:
         print("no onion links")
pass
