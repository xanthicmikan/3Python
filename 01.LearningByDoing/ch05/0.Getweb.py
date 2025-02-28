import requests
r = requests.get('http://www.google.com.tw')

if r.status_code == 200:
    print(r.text)
else:
    print(r.status_code, r.reason) 