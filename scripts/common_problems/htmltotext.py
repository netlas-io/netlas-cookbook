import netlas
import html2text

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `http.body:*phpMyAdmin*`
netlas_query = netlas_connection.query(query="http.body:*phpMyAdmin*")


# iterate over data and print: ip, web page text
for response in netlas_query['items']:
    print (response['data']['ip'])
    print (html2text.html2text(str(response['data']['http']['body'])))   
pass