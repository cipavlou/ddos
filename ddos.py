import requests

url = input("Insert url: ")

while True:
    requests.get(url)
