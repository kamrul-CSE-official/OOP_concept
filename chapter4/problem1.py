import requests  # type: ignore

url = "http://subeen.com/allposts"
response = requests.get(url)

print(type(response))

print(response.ok)
print(response.status_code)
print(response.reson)