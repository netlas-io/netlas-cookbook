import netlas

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `certificate.issuer.street_address:*mcgill*`
netlas_query = netlas_connection.query(query="certificate.issuer.street_address:*mcgill*")


print (type(netlas_query))

# iterate over data and print: ip, url, cetificate issuer 
for response in netlas_query['items']:
    print (response['data']['uri'])
    print (response['data']['certificate']['issuer'])
