import netlas

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `tag.name:"adobe_coldfusion"`
netlas_query = netlas_connection.query(query='tag.name:"adobe_coldfusion"')


# iterate over data and print: IP,URL 
for response in netlas_query['items']:
    print (response['data']['ip'])
    print (response['data']['uri'])
   
pass