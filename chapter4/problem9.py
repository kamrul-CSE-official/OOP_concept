import requests

url = "http://dimikcomputing.com"

response = requests.get(url)

with open("demik.html", "w") as f:
    f.write(response.text)