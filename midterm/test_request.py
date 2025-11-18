import requests

url = "http://127.0.0.1:5001/predict"

data = {
    "area": 2000,
    "bedrooms": 5,
    "bathrooms": 1,
    "stories": 2,
    "parking": 1
}

response = requests.post(url, json=data)
print(response.json())
