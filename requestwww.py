import requests

r=requests.get("https://item.jd.com/100003395467.html")

#r.encoding="utf-8"

print(r.text)