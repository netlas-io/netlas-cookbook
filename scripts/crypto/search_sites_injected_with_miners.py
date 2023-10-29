import netlas

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `http.body:coinhive.min.js domain:*`
netlas_query = netlas_connection.query(query='http.body:coinhive.min.js domain:*')


# iterate over data and print: uri
for response in netlas_query['items']: 
    print (response['data']['uri'])

pass