import requests

url = 'https://httpbin.org/get'
hd = {'user-key': '7ADGS9S'}
pm = {'id': 1023, 'neme': 'mikan'}
r = requests.get(url, headers = hd, params = pm)
print(r.text)