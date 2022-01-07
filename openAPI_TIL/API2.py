# 아래의 두 가지 방법중에 하나로 dict 타입으로 변환이 가능
# json.loads( response.text )
result = response.json()
import requests
import xmltodict

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

lee = pd.DataFrame( result['results'][0]['data'] )
lee.rename( columns={'ratio':'lee'}, inplace=True )
yoon = pd.DataFrame( result['results'][1]['data'] )
yoon.rename( columns={'ratio':'yoon'}, inplace=True )
huh = pd.DataFrame( result['results'][2]['data'] )
huh.rename( columns={'ratio':'huh'}, inplace=True )
ahn = pd.DataFrame( result['results'][3]['data'] )
ahn.rename( columns={'ratio':'ahn'}, inplace=True )
sim = pd.DataFrame( result['results'][4]['data'] )
sim.rename( columns={'ratio':'sim'}, inplace=True )

rawData = pd.merge( left=lee, right=yoon, on='period' )
rawData = pd.merge( left=rawData, right=huh, on='period')
rawData = pd.merge( left=rawData, right=ahn, on='period')
rawData = pd.merge( left=rawData, right=sim, on='period')

plt.figure( figsize=(20,5) )
sns.lineplot(data=rawData, x='period', y='lee', label='lee')
sns.lineplot(data=rawData, x='period', y='yoon', label='yoon')
sns.lineplot(data=rawData, x='period', y='huh', label='huh')
sns.lineplot(data=rawData, x='period', y='ahn', label='ahn')
sns.lineplot(data=rawData, x='period', y='sim', label='sim')

plt.ylabel('trend')
plt.xticks(rotation=30)
plt.legend()

plt.show()

# xml을 파이썬의 dict 형태로 변환
result = xmltodict.parse( response.text )
type( result )

serviceKey = '9Td+AysuLzv3Fq4/SIhE/ri4rGiZiFjD92SQxmfQalI/2vW3xPEOcSNURc+LUMqpgZoCrTL8gD1mXFb1QhXBIg=='
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'

params ={
  'serviceKey' : serviceKey, 
  'pageNo' : '1', 
  'numOfRows' : '10', 
  'startCreateDt' : '20200101', 
  'endCreateDt' : '20220107' 
}

response = requests.get(url, params=params)
print(response.status_code)

result = xmltodict.parse( response.text )

result.keys()

type( result['response'] )
result['response'].keys()
result['response']['header']
result['response']['body'].keys()
print( result['response']['body']['numOfRows'] )
print( result['response']['body']['pageNo'] )
print( result['response']['body']['totalCount'] )
result['response']['body']['items'].keys()
len( result['response']['body']['items']['item'] )
result['response']['body']['items']['item'][-2]

## 데이터 파싱
# 일자별, 지역별, (확진자, 사망자) 수
for row in result['response']['body']['items']['item']:
  print('날짜:', row['createDt'])
  print('지역:', row['gubun'])
  print('사망자 수:', row['deathCnt'])
  print('확진자 수:', row['defCnt'])