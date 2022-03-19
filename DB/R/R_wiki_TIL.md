0204 수업

010-8877-2864 김성환 shwank@nate.com



# 데이터

## 일반적인 데이터의 특징

### 존재론적 특징

- 데이터가 갖고 있는 존재적 특징으로 데이터를 구분

정성적 데이터

- 언어, 문자 등으로 이루어짐

정량적 데이터

- 수치, 도형, 기호 등으로 이루어짐

### 목적론적 특징

- 데이터의 목적론적 특징에 대해 정의

## 수집 데이터의 특징 정의

### 정형 데이터

- 내부 시스템인 경우가 대부분이라 수집이 쉽다
- CRUD가 일어나는 일반적인 아키텍처 구조로 이루어져 있다

### 반정형 데이터

- 보통 API 형태로 제공되기 때문에 데이터 처리 기술이 요구 된다
- 데이터의 메타구조를 해석해 정형 데이터 형태로 바꿀 수 있는 아키텍처 구조를 수정해야 한다

### 비정형 데이터

- 수집 데이터 처리가 어렵다
- 텍스트나 파일을 파싱해 메타구조를 갖는 데이터의 셋형태로 바꾸고 정형 데이터 형태의 구조로 만들 수 있도록 아키텍처 구조를 수정해야 한다



# R

1. R Console 설치

2. 실행 잘되나 확인

   ```
   demo()
   demo(packages)
   ```

3. 자주 사용하는 packages 설치

   - 목록

     ```
     RODBC : DBMS에 연결을 위한 Package
     sqldf  : database의 문법을 사용 가능
     ggplot2 : 구글에서 제공하는 여러 plot  
     rgoogleMaps : 구글에서 제공하는 Map관련 
     googleVis : 여러 시각화 함수 제공
     animation : 동적 시각화 제공
     ```

   - ggplot2 패키지 설치 해보기 

   ```
   # macOS의 경우 xcode 설치 되어있어야함
   # terminal 에서 xcode 설치
   xcode-select --install
   brew install libpng
   # package 설치
   install.packages("ggplot2")
   ```

과제

- 위키독스 - Must Learning with R (개정판)

- Ch3,5,6,7 해보기
- dplyr 패키지 가지고 데이터를 가공해서 가져오기 or 워드클라우드로 데이터 가져오기



## R이란

- 데이터 분석을 위한 무료 분석 Tool

## 엑셀과 R

### 엑셀의 단점

- 대용량 데이터 대해 처리가 어려움(시간이 많이 소요, 멈춤현상)
- 데이터 분석이 제한적

### R의 장점

- 대용량 데이터 처리가 능하다
- 명령어 체계가 매우 자유로움(문법이 자유로움)
- 오픈소스 및 가벼운 프로그램
  - 대부부의 함수는 필요한 패키지를 통해 돌릴 수 있음

### R의 단점

- 메모리를 많이 잡아 먹는다
- 연산속도가 빠른편은 아니다
- 새로운 패키지 사용할때, 설명서를 열심히 읽어야 한다

## Python과 R

- 가볍게 데이터 분석을 실무에 적용시키기에는 R이 적합
- 통계분석에서는 Python보다 R이 코드가 간결하게 짤수 있다.
- 개발쪽으로 넘어가면 Python이 좀 더 적합

## R의 자료형

- 숫자형 : 모든 숫
- 문자형 : 모든 문자
- 논리형 : True&False
- NA & NULL형 : 없음 & 비어있음
- Date & Time :  시간과 날짜 저장
  - `Sys.Date()`,`Sys.time()`,` date()`

## 연산

- `+`,`-`,`*` 
  - 각 원소 끼리 연산됨
- `union(x,y)`
  - 합집합 , 합쳐서 출력(중복되는것은 한번만 출력)
- `setoff(x,y)`
  - 차집합, x만 가지고 있는 요소 출력

- `intersect(x,y)`
  - 교집합, 둘다 가지고 있는 요소



## 벡터의 생성

- - `c()`는 Combind의 약자를 나타내는 명령어, 벡터를 생성하는 사용된다
    - 값이 하나만 들어가있으면 스칼라라고 한다.
  - 데이터가 세로로 저장된다고 생각하면 됨

  ```r
  B = c(2,3,4,5) 
  #1부터 10까지 순차적으로 증가하는 데이터 생성
  x1 = c(1:10) 
  ```

  - rep(), sep()을 통한 벡터 생성

    - 순차적인 수열 생성 sequence의 줄임말로 순차적인 데이터를 생성
    - seq() : seq(from = 시작 숫자 , to = 마지막 숫자, by = 증가범위)

    ```r
    x1_2 = seq(from = 1, to = 10,by = 1)
    x2 = seq(from = 1, to = 10,by = 2) 
    x3 = seq(from = 1, to = 10,length.out = 4) 
    # 1~10안에 4개를 간격이 동일하게 출력된다 
    ```

    - rep()는 repeat의 줄임말로 반복된 데이터를 생성

    ```r
    y = rep(1,10) # 1이 10번 출력됨
    #1,10이 2번 출력됨 / 1 10 1 10
    y2 = rep(c(1,10), 2) 
    y2_times = rep(c(1,10), times = 2)
    # 1 2번, 10 2번 출력됨 / 1 1 10 10
    y3 = rep(c(1,10), c(2,2)) 
    y3_each = rep(c(1,10), each = 2)
    ```



## 행렬(matrix)

- 모든데이터의 타입은 동일
- 벡터를 여러개 합친 형태
- row 와 column으로 이루어짐

```
# 매트릭스는 기본적으로 열을 기준을 들어간다
v1 = c(1,2,3,4)
mat = matrix(v1)
mat

# 열을 기준으로 들어가면서 행의 갯수를 지정
mat = matrix(v1, nrow = 2)
mat

# 행을 기준으로 
mat = matrix(v1, nrow = 2, byrow=T)
mat
```

## 데이터 프레임

- 다양한 데이터 타입을 저장 할 수 있는 자료 형태
- DBMS에서의 테이블과 같은 형태

```
No = c(1,2,3,4)
Name = c("Apple","Peach","Banana","Grape")
Price = c(500, 200, 100, 50)
Qty = c(5,2,4,7)

sales = data.frame(No,Name,Price,Qty)
sales

#테이블 형태로 볼 수 있음
View(sales)

#특정 조건에 맞는 행 추출
subset(sales, Qty>3)
subset(sales, Name == 'Apple')
subset(sales, Price >= 300)

#특정 컬럼만 조회
sales$Name
subset(sales, Price>=100, select = Name)
subset(sales, Qty>3, select = c(Name,Price))
#특정 컬러만 제외
subset(sales, Qty>3, select = -Price)
```



### 실습

- [Must Learning with R (개정판)](https://wikidocs.net/73371)
- Ch3

```
HR = read.csv('/Users/ssimda/workspace/R/HR_comma_sep.csv')
head(HR,n = 3)
str(HR)
summary(HR)

#factor로 변경
HR$Work_accident=as.factor(HR$Work_accident)
HR$left=as.factor(HR$left)
HR$promotion_last_5years=as.factor(HR$promotion_last_5years)

summary(HR$left)

#ifelse

HR$satisfaction_level_group_1 = ifelse(HR$satisfaction_level > 0.5, 'High', 'Low')
HR$satisfaction_level_group_1 = as.factor(HR$satisfaction_level_group_1)
summary(HR$satisfaction_level_group_1)

HR$satisfaction_level_group_2 = ifelse(HR$satisfaction_level > 0.8, 'High', ifelse(HR$satisfaction_level > 0.5,'Mid','Low'))

HR$satisfaction_level_group_2 = as.factor(HR$satisfaction_level_group_2)
str(HR)
summary(HR$satisfaction_level_group_2)

# salary가 high인 직원들만 추출하여 HR_High라는 새로운 데이터 셋을 생성
HR_High = subset(HR,salary == 'high')
summary(HR_High$salary)

HR_High_IT = subset(HR,salary == 'high' & sales == 'IT') 
print(xtabs(~ HR_High_IT$sales + HR_High_IT$salary))

HR_High_IT2 = subset(HR,salary == 'high' | sales == 'IT')
print(xtabs(~ HR_High_IT2$sales + HR_High_IT2$salary))

install.packages("plyr")
library(plyr)

ddply(데이터,집계기준, summarise, 요약 변수)
SS=ddply(HR, # 분석할 Data Set 설정
         c("sales","salary"),summarise, # 집계 기준 변수 설정
         M_SF = mean(satisfaction_level), # 컬럼명 및 계산 함수 설정
         COUNT =length(sales), 
         M_WH = round(mean(average_montly_hours),2))

View(SS)

# 패키지 부착
library(ggplot2) 
library(ggthemes)
install.packages("ggthemes")

ggplot(HR)

ggplot(HR,aes(x = salary))

ggplot(HR,aes(x=salary)) +  geom_bar()

ggplot(HR,aes(x=salary)) +  geom_bar(fill = 'royalblue') 
ggplot(HR,aes(x=salary)) +  geom_bar(aes(fill=salary)) 

# 기본
ggplot(HR,aes(x=satisfaction_level))+geom_histogram()

# 구간 수정 및 색 입히기
ggplot(HR,aes(x=satisfaction_level))+geom_histogram(binwidth = 0.01,col='red',fill='royalblue') 

# 기본
ggplot(HR,aes(x=satisfaction_level))+geom_density()

# 색 입히기
ggplot(HR,aes(x=satisfaction_level))+geom_density(col='red',fill='royalblue') 
# col은 테두리, fill은 채우기박스플롯

ggplot(HR,aes(x=left,y=satisfaction_level)) +geom_boxplot(aes(fill = left)) + xlab("이직여부") + ylab("만족도") + ggtitle("Boxplot") + labs(fill = "이직 여부")
```

- 연습문제

```
# 1. HR 데이터의 행의 수, 열의 수를 구하시오.
str(HR)
# 14999 obs. of  12 variables

#2. salary변수의 strings에 대해 답하시오.
summary(HR$salary)
# low, medium, high

#3.salary변수에 대하여 low는 1, medium은 2, high는 3의 값을 가져 서열정보를 가지게 하는 salary_New 변수를 만드시오.

HR$salary_New = ifelse(HR$salary =='low', 1, ifelse(HR$salary =='medium', 2, 3))
HR$salary_New = as.factor(HR$salary_New)
summary(HR$salary_New)
                                                
#4.Salary_New 값이 2이면서 left는 1인 직원들만 뽑아 Medium_Left라는 새로운 데이터프레임을 만드시오.

Medium_Left = subset(HR, HR$salary_New == '2' & HR$left == '1')
View(Medium_Left)

#5.Medium_Left 데이터에 대해 sales변수 별로 time_spend_company의 평균을 구하여, Time_spend_Mean이라는 새로운 데이터프레임을 만드시오.

library(plyr)
Time_spend_Mean = ddply(Medium_Left, 
                        c("sales"),summarise,
                        M_TSC = mean(time_spend_company))
View(Time_spend_Mean)
```

- Ch5

```
```