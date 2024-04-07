import requests

img_url = "https://goo.gl/pxibBu"

r = requests.get(img_url)

with open("pybook1.png", "w") as f:
    f.write(r.text)
    print(r.text)