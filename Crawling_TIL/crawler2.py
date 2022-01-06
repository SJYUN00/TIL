import requests
from fake_useragent import UserAgent  
agent = UserAgent()
header = {'User-Agent': agent.chrome}

url = 'https://unsplash.com/photos/g9P21WrK_7g/download?ixid=MnwxMjA3fDB8MXxhbGx8NHx8fHx8fDJ8fDE2NDExODI0MTk&force=true'

response = requests.get(url, headers=header)
print( response.content )

with open('web/data/download4.jpg', 'wb') as file:
  file.write( response.content)