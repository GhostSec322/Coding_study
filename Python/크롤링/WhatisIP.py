import requests as req 
res = req.get('http://api.ipify.org/')
print(res.request.method)
print(res.text)