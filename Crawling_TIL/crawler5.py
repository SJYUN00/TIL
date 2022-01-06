from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# webdriver
# 크롬을 기준으로 현재 사용하고 있는 버전에 맞춰서 webdriver를 다운로드
service = Service(executable_path="c:\\Users\\UserK\\syun\\work_space\\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)

url = 'http://itempage3.auction.co.kr/DetailView.aspx?itemno=C253239668'
browser.get( url )

review_button = browser.find_element(By.CSS_SELECTOR, 'li#tap_moving_2 a')
review_button.click()

elements = browser.find_elements(By.CSS_SELECTOR, 'ul.list__review p.text')
for element in elements:
  print(element.text)