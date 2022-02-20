from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# webdriver
# 크롬을 기준으로 현재 사용하고 있는 버전에 맞춰서 webdriver를 다운로드
service = Service(executable_path="c:\\Users\\UserK\\syun\\work_space\\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)

url = 'https://lc.multicampus.com/k-digital/#/login'
browser.get( url )

time.sleep(2)
inputs = browser.find_elements(By.CSS_SELECTOR, 'div.input-row-line input')
loginButton = browser.find_element(By.CSS_SELECTOR, 'div.btn-row button.login-btn')
inputs[0].send_keys('pender00')
inputs[1].send_keys('Tjdwns2516')

loginButton.click()

time.sleep(10)

last_height = browser.execute_script('return document.body.scrollHeight')
while True:
  browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
  time.sleep(2)
  new_height = browser.execute_script('return document.body.scrollHeight')
  if new_height == last_height: break
  last_height = new_height

articles = browser.find_elements(By.CSS_SELECTOR, 'div.feedlist span article')
for article in articles:
  for content in article.find_elements(By.CSS_SELECTOR, 'span.feedContentB1k span'):
    print(content.text)