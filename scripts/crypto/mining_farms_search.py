import netlas

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `http.headers.www_authenticate:antMiner`
netlas_query = netlas_connection.query(query='http.headers.www_authenticate:antMiner')


# iterate over data and print: uri, http headers
for response in netlas_query['items']: 
    print (response['data']['uri'])
    print (response['data']['http']['headers'])

pass
