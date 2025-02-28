from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get('http://www.google.com')
print('title：' + browser.title)
print('web：' + browser.current_url)
print('content：' + browser.page_source[0:50])
print('window：', browser.get_window_rect())
browser.save_screenshot('C:/Users/mika/Desktop/scrcap.png')
sleep(3)
browser.set_window_rect(200, 100, 500, 250)
sleep(3)
browser.fullscreen_window()
sleep(3)
browser.quit()