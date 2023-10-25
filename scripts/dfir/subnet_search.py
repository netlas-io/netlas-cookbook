import netlas

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `a:"163.114.132.0/24"`
netlas_query = netlas_connection.query(query='a:"163.114.132.0/24"',datatype="domain")


# iterate over data and print: domain
for response in netlas_query['items']: 
    print (response['data']['domain'])
pass