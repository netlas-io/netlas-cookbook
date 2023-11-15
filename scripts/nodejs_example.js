fetch('https://app.netlas.io/api/domains/?q=ivanov.com&source_type=include&start=0&fields=*', {
  headers: {
      "X-API-Key": "YOUR_API_KEY",
  },
})
    .then((response) => response.text())
    .then((body) => {

        var jsonArray = JSON.parse(body);
        console.log(jsonArray['items'][0]);
    }); 
