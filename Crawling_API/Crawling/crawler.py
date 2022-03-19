import urllib.request
from fake_useragent import UserAgent

agent = UserAgent()

# urllib은 urlretrieve함수를 이용해서 한 번에 파일로 저장
url = 'https://image.zdnet.co.kr/2022/01/01/e601fd8d72cc33ca75cd9d41d3315684.jpg'

# 파일을 저장할 경로
path = 'web/data/download.jpg'
# opener 객체를 생성해서 헤더를 수정을 먼저 해줍니다.
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', agent.chrome)]
urllib.request.install_opener(opener)
urllib.request.urlretrieve( url, path )
