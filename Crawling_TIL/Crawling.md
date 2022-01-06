# 크롤링(Crawling)
- 크롤링 Vs. 스크래핑
  - 두 용어에서 큰 차이를 두지 않고, 대표적으로 크롤링 이라는 이름으로 주로 사용
  - 구분은 가능합니다.

1. 웹 사이트에서 내용을 가져오는 방법
  - 웹 사이트에 존재하는 거의 대부분의 내용들을 가져올 수 있습니다. 
  - 텍스트, 영상, 음성, 그림, ... 
  - **주의!**
    - 마음대로 가져다가 사용해도 되는건 아닙니다.
    - 특히 **저작권**과 관련해서 문제가 발생할 수 있습니다.
    - 다운로드만 해도 불법인 경우가 있고
    - 배포가 되었을 경우에 불법인 경우가 있습니다.
      - 배포할 의도가 없었어도 배포가 되면 불법이에요
      - P2P같은 경우가 그런 경우가 많이 있습니다.
      - 변명의 여지가 없어요
    - 과도한 트랙픽을 유발할 수 있기 때문에, 관리자는 싫어합니다.
      - 일반적으로 웹 서버 관리자들은 크롤링을 허용하지 않습니다.
      - 모니터링을 통해서 차단을 합니다.

2. 오픈 API를 통해서 가져오는 방법
  - 가장 추천하는 방법 입니다.
  - 수집을 허용하기 때문에 API가 제공

## 소켓프로그래밍을 이용한 HTTP 통신
- 크롤링이란? HTTP를 이용해서 원하는 자원(파일, 그림, 영상, 텍스트, ... )을 가져오는 방법
  - 일반적으로는 웹 페이지(html)를 주로 요청
  - 그림 파일(jpg, png, ...)일 수도 있는거고
  - 여러가지 형태의 파일들을 HTTP 통신을 이용해서 가져올 수 있다. 


## 라이브러리를 이용한 HTTP 통신
- 소켓 프로그래밍을 직접 하지 않고도 편하게 HTTP 통신을 구현할 수 있습니다. 
  - urllib
  - requests

### urllib을 통한 HTTP 통신
- 파이썬 기본 패키지
- 따로 설치가 필요없이 바로 사용이 가능

### urllib을 통한 파일 저장
- urllib은 리퀘스트 객체를 생성할 때, 헤더값을 직접 정의
  - fake_agent를 이용해서 `user-agent` 헤더의 값을 크롬 크라우저의 값과 동일하게 설정
  ```
  prompt> pip install fake_useragent
  ```

  import urllib.request
from fake_useragent import UserAgent

# 파이썬이 아닌 웹 브라우저를 통해서 요청하는 것 처럼 보이기 위해
# 헤더값을 직접 설정해줍니다.
agent = UserAgent()
header = {'User-Agent': agent.chrome}

url = 'https://image.zdnet.co.kr/2022/01/01/e601fd8d72cc33ca75cd9d41d3315684.jpg'
request = urllib.request.Request( url, headers=header )
response = urllib.request.urlopen( request )
print(response.read())


파일에 대한 접근이 자유롭다면 별다른 설정없이 바로 다운로드 해볼 수 있습니다. 

### requests을 통한 HTTP 통신
- 설치가 필요한 패키지 이지만, 콜랩에서는 미리 설치가 되어 있기 때문에 바로 사용이 가능합니다. 
  - 로컬에서 사용하는 경우에는 따로 설치를 해주면 됩니다. 

  ```
  prompt> pip install requests
  ```

- [requests 홈페이지](https://docs.python-requests.org/en/master/)

requests를 통한 파일 저장
[ ]
import requests
from fake_useragent import UserAgent

agent = UserAgent()
header = {'User-Agent':agent.chrome}

url = 'https://image.zdnet.co.kr/2022/01/01/e601fd8d72cc33ca75cd9d41d3315684.jpg'

response = requests.get(url, headers=header)
print( response.content )
파일로 저장하는 경우에는 바이너리형태로 파일 객체를 생성하고 저장

[ ]


# 스크래핑(Scraping)
- 웹 페이지에서 내가 원하는 내용만 가져오는 기능
  - 크롤링된 웹 페이지에서 내가 원하는 내용을 찾는 것(파싱)
  - 수업 시간에는 네이버 영화 페이지의 사용자 리뷰만 가져와보도록 합니다. 

## 네이버 영화 리뷰 페이지 크롤링
- 크롤링된 HTML내에 내가 원하는 `사용자 리뷰`가 있을겁니다. 
- 이 HTML로부터 내가 원하는 요소를 찾는겁니다(파싱)


## BeatifulSoup
- CSS 셀렉터를 이용해서 원하는 요소를 검색할 수 있습니다. 
- 설치

```
prompt> pip install bs4
```


### select
- select는 find_all과 동일한 기능
- select_one은 find와 동일한 기능
- CSS Selector를 이용해서 요소를 선택

# SELENIUM
- 기본적인 사용법

```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# webdriver
# 크롬을 기준으로 현재 사용하고 있는 버전에 맞춰서 webdriver를 다운로드
service = Service(executable_path="c:\\IJH\\workspace\\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)

url = 'https://www.naver.com'
browser.get( url )

# 검색어 입력 후 엔터 입력
# element = browser.find_element(By.CSS_SELECTOR, 'input#query')
# element.send_keys('검색어')
# element.send_keys('\n')

# 검색어 입력 후 마우스 클릭
# 클릭 가능한 요소라면 클릭이 가능
input = browser.find_element(By.CSS_SELECTOR, 'input#query')
button = browser.find_element(By.CSS_SELECTOR, 'button#search_btn')
input.send_keys('검색어')
button.click()

input2 = browser.find_element(By.CSS_SELECTOR, 'input#nx_query')
input2.clear()
input2.send_keys('두번째 검색어')
```
