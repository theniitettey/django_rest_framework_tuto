import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://www.httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api"


get_reponse = requests.post(endpoint, json={"title": "Hello world"}) # API -> Application Programming Interface
# print(get_reponse.text)
# print(get_reponse.json())
print(get_reponse.json())

