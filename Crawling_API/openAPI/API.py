# 반드시 개별적으로 전달받은 키를 사용을 해야 합니다.
clientID = 'mXITqCogjHV9rXscXrQ1'
clientSecret = 'pUelfdpkSp'

import requests
import json

url = 'https://openapi.naver.com/v1/datalab/search'
header = {
  'X-Naver-Client-Id': clientID,
  'X-Naver-Client-Secret': clientSecret,
  'Content-Type': 'application/json'
}

data = {
  'startDate':'2021-01-01',
  'endDate':'2021-12-31',
  'timeUnit':'week',
  'keywordGroups':[
    {
      'groupName':'이재명',
      'keywords':['더불어민주당', '이재명']
    },
    {
      'groupName':'윤석열',
      'keywords':['국민의힘', '윤석열']
    }, 
    {
      'groupName':'허경영',
      'keywords':['국가혁명당', '허경영']
    },
    {
      'groupName':'안철수',
      'keywords':['국민의당', '안철수']
    },
    {
      'groupName':'심상정',
      'keywords':['정의당', '심상정']
    }
  ],
  'ages':['3', '4', '5', '6', '7', '8', '9', '10', '11']
}

jsonData = json.dumps(data)
response = requests.post( url, data=jsonData, headers=header )
print( response.status_code )

response.json()



url = 'https://openapi.naver.com/v1/datalab/search'
header = {
  'X-Naver-Client-Id': clientID,
  'X-Naver-Client-Secret': clientSecret,
  'Content-Type': 'application/json'
}

data = {
  'startDate':'2021-01-01',
  'endDate':'2021-12-31',
  'timeUnit':'month',
  'keywordGroups':[
    {
      'groupName':'후보자',
      'keywords':['이재명', '윤석열', '허경영', '심상정', '안철수']
    },
    {
      'groupName':'정당',
      'keywords':['국민의힘', '더불어민주당', '국가혁명당', '국민의당', '정의당']
    }
  ],
  'ages':['3', '4', '5', '6', '7', '8', '9', '10', '11']
}