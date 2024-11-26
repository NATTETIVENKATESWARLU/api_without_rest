import requests
BASE_URL='http://127.0.0.1:8000/'
END='api_json4'
reson=requests.get(BASE_URL + END)
data=reson.json()
print(data)

