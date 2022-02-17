# 전처리할 자료 불러오기
sat = pd.read_csv('/content/drive/MyDrive/프로젝트/data/삶의_만족도_시도(https:  kosis.kr statisticsList statisticsListIndex.do?menuId=M_01_03_01&vwcd=MT_GTITLE01&parmTabId=M_01_01&parentId=112.1;&outLink=Y).csv', encoding='cp949')

# 전국단위의 인덱스를 제거합니다
sat.drop(index=[1,2,3],inplace=True)

# 인덱스 제거 후 재정렬합니다.
sat.reset_index(drop=True, inplace=True)

# 전체는 남기고 성별로 구별한 인덱스는 제거해줍니다.
for i in range(1, 52):
  if i%3 == 1: continue
  sat.drop(index=[i], inplace=True)

# 특성별 컬럼은 삭제해줍니다.
sat.rename(columns={'행정구역별(1)':'지역'}, inplace = True)
sat.drop(['특성별(1)', '특성별(2)'], axis = 1, inplace = True)

# 매우만족에는 5점, 약간만족은 4점, 보통은 3점, 약간불만족은 2점, 매우불만족은 1점으로 부가하여

# 지역별 평균을 낸 후, 만족도의 총량을 비교해보는 방식을 이용합니다.
for i in range(13):
  sat.drop([f'{i+2009}'], axis = 1, inplace = True)

# 세종시 데이터 결측치에 0.0 값을 넣어줍니다
for col in sat.columns[1:]: 
  if col == '2015.1' : break 
  sat.at[22,col] = 0.0

# 행정구역별 인덱스를 제거합니다. 만족도별 평균을 낼것이므로 더이상 불필요합니다.
sat.drop(index=[0], inplace=True)

# 문자형으로된 숫자들을 실수형으로 처리해줍니다.
for col in sat.columns[1:]:
  sat = sat.astype({col:'float'})

# 인덱스 정렬이 안되어있으므로 정렬해줍니다.
sat.reset_index(drop=True, inplace=True)
sat_avg.reset_index(drop=True, inplace=True)

# 매우만족에 5점, 만족에 4점, 보통은 3점, 불만족은 2점, 매우불만족은 1점을 부여해 평균치를 계산하는 코드를 작성 및 실행합니다.
sat_avg = deepcopy(sat)
for i in range(13):
  sat_avg[f'{i+2009}'] = 0.0
for k in range(17): # 행
  for i in range(13): # 연도 
    sat_avg[f'{i+2009}'][k] = round((sat.iloc[k, i*5+1] * 5 + sat.iloc[k, (i*5)+2] * 4 + sat.iloc[k, (i*5)+3] * 3 + sat.iloc[k, (i*5)+4] * 2 + sat.iloc[k, (i*5)+5] * 1)/5 , 2)
sat_avg

# 계산을 마친 후 평균값을 제외한 데이터는 삭제해줍니다.
for col in sat_avg.columns[1:] : 
  if col == '2009': break    
  del sat_avg[col]

# 이전에 처리하지 못한 지역을 행정구역으로 변경해줍니다.
sat_avg.rename(columns={'지역':'행정구역'}, inplace=True)

# 전국, 수도권, 지방의 인덱스를 추가해줍니다.
sat_avg.loc[17] = sat_avg.loc[0]
sat_avg.loc[18] = sat_avg.loc[0]
sat_avg.loc[19] = sat_avg.loc[0]
sat_avg.loc[17, '행정구역'] = '전국'
sat_avg.loc[18, '행정구역'] = '수도권'
sat_avg.loc[19, '행정구역'] = '지방'

# 전국, 수도권, 지방의 평균값을 구합니다.
for i in range(1, len(sat_avg.columns)):
  sat_avg.iloc[17, i] = sat_avg.iloc[0:17, i].mean()
  sat_avg.iloc[18, i] = sat_avg.iloc[[0, 3, 8], i].mean()
  sat_avg.iloc[19, i] = sat_avg.iloc[[1,2,4,5,6,7,9,10,11,12,13,14,15,16], i].mean()

# 하위 인덱스를 상위로 끌어올린후 재정렬해줍니다.
sat_avg = sat_avg.reindex(index=[17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
sat_avg.reset_index(drop=True, inplace=True)
sat_avg.iloc[:, 1:] = sat_avg.iloc[:, 1:].round(decimals=2) #소수점 둘째자리까지 나타내줍니다.

# 파일을 저장합니다
pd.DataFrame(sat_avg).to_csv('/content/drive/MyDrive/프로젝트/[D9&10] 데이터시각화 프로젝트_4조/윤성준/삶의만족도(최종)', index=False)

데이터 전처리과정이 복잡했지만? 필요한 부분 누락없이 한다면 할만한 작업인듯?하다..