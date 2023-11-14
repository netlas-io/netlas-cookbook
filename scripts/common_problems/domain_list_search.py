import netlas

apikey = "YOUR_API_KEY"

# create new connection to Netlas
netlas_connection = netlas.Netlas(api_key=apikey)


# read file domains.txt line by line
with open("scripts/common_problems/domains.txt") as f:
    # save each line to domain variable
    for domain in f:
         # retrieve data from responses by query `domain:domainname`
        netlas_query = netlas_connection.query(
            query=f"domain:{domain}", datatype="domain-whois"
        )


        # iterate over data and print:  ip, isp
        for response in netlas_query['items']:
            print (response['data']['ip'])
            print (response['data']['isp'])