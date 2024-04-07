import requests

image_url = "https://goo.gl/psibBu"

r = requests.get(image_url)

with open("pybook1.png", "wb") as f:
    f.write(r.content)