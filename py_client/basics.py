import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
# endpoint = 'http://localhost:8000/'
endpoint = 'http://localhost:8000/api/'

get_response = requests.get(endpoint, params={'abc': 123},  json={"product_id": 123}) # HTTP Request, json optional parameter will send a data object to the output
# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
