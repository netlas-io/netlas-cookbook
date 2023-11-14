import netlas
from bs4 import BeautifulSoup

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `http.body:shop`
netlas_query = netlas_connection.query(query="http.body:shop")


# iterate over data and print: URL, h1 tags from body
for response in netlas_query['items']:
    print (response['data']['uri'])
    soup = BeautifulSoup(response['data']['http']['body'], "html.parser")
    try:
        print(soup.find("h1").get_text())
    except Exception:
        print("no h1 tags")
pass