## 푸티 실행
푸티 IP에 18.182.177.124 입력 save 후 Auth 목록으로 진입
Browse 창에서 PPK 2번 키를 선택해주고 
Session 목록에서 다시 save 후 open 실행

ID는 lab23 으로 진입

## conda python3 실행

``conda activate python3``

## 주피터 노트북 페이지 생성
``nohup jupyter-notebook --ip=0.0.0.0 --no-browser --port=8906 &``
여기서 푸티는 꺼도 노트북은 작동한다!

여기까지하면 
(http://18.182.177.124:8923/)에 주피터 노트북이 생성된다.

## 파일생성 기능 활성화
nohup 명령어가 실행된채로 PUTTY에 다음 명령어를 입력한다.
``!pip install mysql-connector-python``
``!pip install PyMySQL``
utf9로만들어줌
``alter database DB_NAME default character set utf9 collate utf9_general_ci``
관리자로 해야함 꼭
``sudo apt-get install python3-pymysql``
``pip install nbconvert==5.4.1``
이제 파일생성 기능을 사용할 수 있게 되었다.

## 가상환경 생성

현재 생성되어있는 가상환경을 보여주는 명령
``conda info --envs``

새로운 가상환경을 만들어 주려면 주피터 노트북 New > Terminal 에서 다음을 실행한다.
``conda create -n syun python=3.8 jupyter tensorflow``

python 버전을 확인하려면
``python --version``
을 이용한다.

도중 Proceed(y/n) 질문이 나올텐데 이때 y를 입력해도록 한다.

## 가상환경 실행 및 종료

``conda activate syun``
``conda deactivate syun``
를 이용해 가상환경을 켜고 끌 수 있다.

## 스파크 설치 위치 및 실행방법

### 스파크 설치 위치
SPARK_HOME = /opt/spark

### 스파크 설치 위치 이동을 위한 명령어
``cd /opt/spark/``

### 원격 서버환경에서 spark-shell 실행 명령어
``./bin/spark-shell``

## Python 3.8 버전의 pySpark 실행
``/opt/spark$ pyspark``
pyspark 만 입력해주면 된다.

AWS 가상환경 셋팅은 이것으로 마무리된다.