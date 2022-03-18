from xml.dom.pulldom import END_DOCUMENT
import pandas as pd
import requests
from bs4 import  BeautifulSoup
from datetime import datetime
import re
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map
import math
from time import sleep
from multiprocessing.dummy import Pool
import multiprocessing as mp
from multiprocessing.pool import MaybeEncodingError

#매일경제 검색 url
start_date = "y1=2019&m1=03&d1=01"
end_date = "y2=2019&m2=08&d2=31"
url = "https://find.mk.co.kr/new/search.php?pageNum={}&cat=&cat1=&media_eco=&pageSize=10&sub=all&dispFlag=OFF&page=news&s_kwd=%C1%D6%BD%C4&s_page=news&go_page=&ord=1&ord1=1&ord2=0&s_keyword=%C1%D6%BD%C4&period=p_direct&s_i_keyword=%C1%D6%BD%C4&s_author=&{}&{}&ord=1&area=ttbd"

def get_list(idx) :
 
  #idx = 검색했을때 page 번호
  req = requests.get(url.format(idx, start_date, end_date))

  #한글깨져서 인코딩 지정해줘야함
  soup =  BeautifulSoup(req.content.decode('euc-kr','replace'), 'html.parser')
  div_list = soup.find_all('div', {'class' : 'sub_list'})
  art_list = [i.find('span', {'class': 'art_tit'}) for i in div_list]

  #db에 저장할거 title, href, body, date
  df = pd.DataFrame(columns = {'title','href', 'date','body'})
  for article in art_list:
    append_flag = True


    title = str(article.find("a").contents[0])
    href = str(article.find("a")["href"])
    body_text = None
    date = None
    try:
      req = requests.get(href, timeout=2)
    except requests.exceptions.Timeout as errd:
      print("Timeout Error : ", errd)
      pass
    except requests.exceptions.ConnectionError as errc:
      print("Error Connecting : ", errc)
      pass

    except requests.exceptions.HTTPError as errb:
      print("Http Error : ", errb)
      pass
    # Any Error except upper exception
    except requests.exceptions.RequestException as erra:
      print("AnyException : ", erra)
      pass

    try:
      soup =  BeautifulSoup(req.content.decode('euc-kr','replace'), 'html.parser')
    except:
      print("parser error")
      pass

  
    date_text = soup.find('li', {'class' : 'lasttime'})
    if not date_text :
      date_text = soup.find('li', {'class' : 'lasttime1'})
    if date_text :
      match = re.search(r'\d{4}.\d{2}.\d{2}', date_text.string)
      if match :
        date = datetime.strptime(match.group(), '%Y.%m.%d').date()
      else :
        print("match none")
    else :
      append_flag = False
      #print("mssing date text")


    art_text = soup.find('div', {'class' : 'art_txt'})  
    if not art_text :
      art_text = soup.find('div', {'class' : 'article_body'}) 
    if not art_text :
      art_text = soup.find('div', {'class' : 'view_txt'}) 
    if art_text :
      body_text = art_text.get_text()
    else :
      append_flag = False
      #print("mssing body text")
      #print("link : " + href)

    if append_flag : 
      temp = pd.DataFrame({'title' : [ title ], 'href' : [ href ], 'date' : [ date ], 'body' : [body_text]})  
      df = df.append(temp)

  return df

def get_count() :
  req = requests.get(url.format(1, start_date, end_date))
  #한글깨져서 인코딩 지정해줘야함
  soup =  BeautifulSoup(req.content.decode('euc-kr','replace'), 'html.parser')
  count_text = soup.find('span', {'class' : 'class_tit'}).get_text().replace(",","")
  art_count = re.search("\d+",count_text)
  "y1=2019&m1=03&d1=15"

  print(start_date[3:7]+"년 "+start_date[11:13]+"월 "+start_date[17:]+"일 부터 "
  +end_date[3:7]+"년 "+end_date[11:13]+"월 "+end_date[17:]+"일 까지 총 "
  +art_count.group(0)+"개의 기사")

  return art_count.group(0)

if __name__ == "__main__":

  count = get_count()
  tasks_count = math.ceil(float(count)/20) + 1
  
  #tasks = range(1,10)
  tasks = range(1,tasks_count)
  result_list = process_map(get_list, tasks,max_workers=4)
  df = pd.concat(result_list)
  #df = pd.concat(parmap.map(get_list, tasks, pm_pbar = True, pm_processes = 4))

  print(df)     
  file_name = start_date[5:7]+start_date[11:13]+start_date[17:]+"_"+end_date[5:7]+end_date[11:13]+end_date[17:]
  df.to_csv(file_name+'.csv', index = False, encoding='utf-8-sig')