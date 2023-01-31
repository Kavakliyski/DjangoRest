import requests

endpoint = "http://127.0.0.1:8000/"
endpointAPI = "http://127.0.0.1:8000/api/"


# API -> Method
get_response = requests.get(endpointAPI, params={'abc': 123}, json={"query": "Hello world!"})

# print(get_response.text)
# print(get_response.status_code)

print(get_response.json())
