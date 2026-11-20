const apiKey = process.env.NETLAS_API_KEY;
if (!apiKey) {
    console.error('Set NETLAS_API_KEY to your Netlas API key.');
    process.exit(1);
}

const url = new URL('https://app.netlas.io/api/domains/');
url.searchParams.set('q', 'domain:netlas.io');

fetch(url, {
    headers: { Authorization: `Bearer ${apiKey}` },
    signal: AbortSignal.timeout(30_000),
})
    .then((response) => {
        if (!response.ok) {
            throw new Error(`Netlas returned HTTP ${response.status}`);
        }
        return response.json();
    })
    .then((body) => console.log(body.items[0] ?? 'No results.'))
    .catch((error) => {
        console.error(error.message);
        process.exitCode = 1;
    });
