import requests # type: ignore

res = requests.get("http://dmikcomputing.com/abc.html")

print(res.ok)
print(res.reason)
print(res.status_code)