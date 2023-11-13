import netlas
import re

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `http.body:shop`
netlas_query = netlas_connection.query(query="http.body:shop")


# iterate over data and print: URL, emails from body
for response in netlas_query['items']:
    print (response['data']['uri'])
    emails = re.findall("[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+", response['data']['http']['body'])  
    try:
         print(emails)
    except:
         print("no emails")
pass