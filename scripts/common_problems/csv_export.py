import netlas
import csv

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)

# retrieve data from responses by query `http.meta:nazar`
netlas_query = netlas_connection.query(query="http.meta:nazar")

# Create and open CSV file with results
csv_file = open('netlas_results.csv', 'w')

# Create CSV writer object
writer = csv.writer(csv_file, delimiter =';')


# Create a list with data headers:
header = ['IP', 'URL', 'Title']

# Write headers to CSV file
writer.writerow(header)

# iterate over data and print: ip and url to CSV file
for response in netlas_query['items']:

    # Create a list with one line of data:
     data = [response['data']['ip'], response['data']['uri']]
    # Write line to file
     writer.writerow(data)   
pass

# Close CSV file
csv_file.close()
