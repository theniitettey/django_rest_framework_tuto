import requests

product_id = input("what is the prodcut id you want to delete?\n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not a valid id")


if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_resposne = requests.delete(endpoint)

    print(get_resposne.status_code, get_resposne.status_code == 204)