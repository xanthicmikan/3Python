#pip install bs4
#pip install lxml
page = """
<html>
  <head><title>Test</title></head>
  <body>
    <div class="section" id="main">
      <p>Fruit</p>
      <button id="lemon"><h4 class="bk">Lemon</h4></button>
      <button id="lychee"><h4 class="pk">Lychee</h4></button>
      <button id="banana"><h4 class="pk">Banana</h4></button>
    </div>
    <div class="section" id="footer">
      <p>Powered by Mikan</p>
      <a href="https://github.com/xanthicmikan">Contact me</a>
    </div>
  </body>
</html>
"""

from bs4 import BeautifulSoup
bs = BeautifulSoup(page, 'lxml')

print(bs.title)
print(bs.a)

print(bs.a.text)
print(bs.a.get('href'))
print(bs.a['href'])

print(bs.find('h4'))
print(bs.find('h4', {'class': 'pk'}))
print(bs.find('h4').text)

print(bs.find_all('h4'))
print(bs.find_all('h4', {'class': 'pk'}))

print(bs.find_all(['title', 'p']))
print(bs.find_all(['title', 'p'])[1].text)

print('h4:', bs.select('h4'))
print('#book:', bs.select('#books'))
print('.pk:', bs.select('.pk'))
print('h4.bk', bs.select('h4.bk'))

print(bs.select('#main button .pk'))

print(bs.select('#main button .pk')[1].text)
print(bs.select('#footer a')[0]['href'])

