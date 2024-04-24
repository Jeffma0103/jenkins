import requests

res = requests.get("https://play.kkbox.com/discover/featured")
print(res.text)