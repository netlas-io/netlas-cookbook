import netlas

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `uri:*lidl.* AND http.body:pdf`
netlas_query = netlas_connection.query(query='uri:*lidl.* AND http.body:pdf')


# iterate over data and print: uri, body
for response in netlas_query['items']: 
    print (response['data']['uri'])
    print (response['data']['http']['body'])