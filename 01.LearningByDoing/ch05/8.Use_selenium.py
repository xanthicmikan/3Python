#pip install selenium
from selenium import webdriver
from time import sleep
browser = webdriver.Chrome() 
browser.get('http://www.google.com.tw')
sleep(5)
browser.close()
