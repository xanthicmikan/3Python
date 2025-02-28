from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('prefs',
                            {'profile.default_content_setting_values': {'notifications': 2}})
browser = webdriver.Chrome(options=opt)

browser.get('http://www.facebook.com')
browser.find_element(By.ID,"email").send_keys('abc@yahoo.com')
browser.find_element(By.ID,"pass").send_keys('123')
#browser.find_element(By.ID,"login").click()
sleep(10)
