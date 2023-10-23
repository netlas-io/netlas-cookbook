import netlas

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `smtp.banner:fornex.cloud`
netlas_query = netlas_connection.query(query="smtp.banner:fornex.cloud")


# iterate over data and print: SMTP banner, URL, ISP
for response in netlas_query['items']:
    print (response['data']['smtp']['banner'])
    print (response['data']['uri'])
    print (response['data']['isp'])
pass