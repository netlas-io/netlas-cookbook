import netlas
import idna

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `domain:*.中国  OR host:*.中国 `
netlas_query = netlas_connection.query(query="domain:*.xn--fiqs8s OR host:*.xn--fiqs8s")


# iterate over data and print: ip, domain (decoded from punycode)
for response in netlas_query['items']:
    print (response['data']['ip'])
    decoded_domain = idna.decode(str(response['data']['domain'][0]))
    print (decoded_domain)
pass