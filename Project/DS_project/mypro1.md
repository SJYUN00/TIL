# 전처리할 자료 불러오기

unapt = pd.read_csv('unapt = pd.read_csv('/content/drive/MyDrive/프로젝트/data/미분양주택현황_시도_시_군_구(https:  kosis.kr statisticsList statisticsListIndex.do?menuId=M_01_03_01&vwcd=MT_GTITLE01&parmTabId=M_01_01&parentId=107.1;&outLink=Y).csv', encoding='cp949')', encoding='cp949')

# 비교대상 파일의 인덱스 명칭을 수정해줍니다.

unapt['구분'] = ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시','경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']

# 불필요하다고 판단되는 시군구라는 열을 삭제합니다.

unapt.drop(['시군구'], axis = 1, inplace = True)

# 2000년도부터 2006년까지의 데이터는 1월부터 11월의 미분양 주택수가 표기가 되어있지않습니다.
# 그렇기 때문에 12월을 기준으로 미분양된 주택의 수를 데이터화 합니다.
# 2007~2020년 데이터 간소화
# 2021년은 10월까지만 자료가 있으므로 따로 처리를 해줍니다.

# 2000년도부터 2006년의 자료는 12월뿐이므로 따로 처리합니다.
for i in range(1,7):                        
  unapt_Dec[f'{i+2000}'] = 0             
  for j in range(len(unapt_Dec)):         
    unapt_Dec[f'{i+2000}'][j] = unapt_Dec.iloc[j, i]

# 2007년01월 이전의 자료는 삭제해줍니다.

for col in unapt_Dec.columns[1:]:  
  if col == '2007. 01' : break  
  del unapt_Dec[col]

# 각 해의 12월자료만 추출하는 코드를 작성합니다

for i in range(1,15):                        
  unapt_Dec[f'{i+2006}'] = 0             
  for j in range(len(unapt_Dec)):         
    unapt_Dec[f'{i+2006}'][j] = unapt_Dec.iloc[j, i*12]

# 2021년은 10월의 자료를 기준으로 할 것이기 때문에 그 이전의 자료는 삭제합니다.

for col in unapt_Dec.columns[1:]:  
  if col == '2021. 01' : break  
  del unapt_Dec[col]

# 2001년자료는 없으므로 2000년으로 수정합니다.

unapt_Dec.rename(columns={'2001':'2000'}, inplace = True)

# 2021년 10월의 자료만 추출하는 코드를 작성합니다.

unapt_Dec['2021'] = 0           
for j in range(len(unapt_Dec)):         
   unapt_Dec['2021'][j] = unapt_Dec.iloc[j, 10]

# 최종적으로 2021년의 월별자료를 삭제해줍니다.
for col in unapt_Dec.columns[1:]:  
  if col == '2000' : break  
  del unapt_Dec[col]