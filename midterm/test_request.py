import requests

url = "http://127.0.0.1:5001/predict"

data = {
    "area": 1500,
    "bedrooms": 4,
    "bathrooms": 1,
    "stories": 3,
    "parking": 1
}

response = requests.post(url, json=data)
print(response.json())
