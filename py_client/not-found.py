import requests

endpoint = "http://localhost:8000/api/products/1999545454"

get_response = requests.get(endpoint)

try:
    print(get_response.json())
except Exception as e:
    print(f"Error: {e}")