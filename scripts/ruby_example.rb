require 'net/http'
require 'uri'
require 'json'

api_key = ENV['NETLAS_API_KEY']
abort 'Set NETLAS_API_KEY to your Netlas API key.' if api_key.nil? || api_key.empty?

uri = URI('https://app.netlas.io/api/domains/')
uri.query = URI.encode_www_form(q: 'domain:netlas.io')
request = Net::HTTP::Get.new(uri)
request['Authorization'] = "Bearer #{api_key}"

response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true, open_timeout: 30, read_timeout: 30) do |http|
  http.request(request)
end
abort "Netlas returned HTTP #{response.code}" unless response.is_a?(Net::HTTPSuccess)

result = JSON.parse(response.body)
puts result.dig('items', 0, 'data', 'domain') || 'No results.'
