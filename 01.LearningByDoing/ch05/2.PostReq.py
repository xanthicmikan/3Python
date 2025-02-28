import requests

url = 'http://httpbin.org/post'
r = requests.post(url, data = 'Hello')
print(r.text)
r = requests.post(url, data = {'id':'666', 'name':'Mikan'})
print(r.text)