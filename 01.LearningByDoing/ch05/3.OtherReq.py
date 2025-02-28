import requests

#put
r = requests.put('https://httpbin.org/put', data = {'key':'qaz'})
print(r.text)
#patch
r = requests.patch('https://httpbin.org/patch', data = {'key':'wsx'})
print(r.text)
#delete
r = requests.delete('https://httpbin.org/delete')
print(r.text)