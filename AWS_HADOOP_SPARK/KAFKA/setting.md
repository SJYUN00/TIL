# 카프카 세팅

## Zookeeper 다운
wget (zookeeperURL)

## 압축해제
tar xvf apache-zookeeper-3.5.9-bin.tar.gz

## 소프트링크 연결
ln -s zookeeper-3.5.9-bin.tar zookeeper

## 모두 정지, status 확인
./all_stop.sh
all_check.sh

## 주키퍼 conf내 zoo.cfg 파일 생성 및 정보 수정
cd zookeeper
cd conf

cp zoo_sample.cfg zoo.cfg
nano zoo.cfg
dataDir=/home/hadoop/zookeeper/data

## 주키퍼 서버 실행, 클라이언트 실행 확인 및 종료
cd ..
bin/zkServer.sh start
bin/zkCli.sh
quit

bin/zkServer.sh stop

## 주키퍼 conf/zoo.cfg 파일 수정
cd conf
nano zoo.cfg

tickTime=2000
initLimit=10
syncLimit=5
dataDir=/home/hadoop/zookeeper/data
clientPort=2181
server.1=server01:2888:3888
server.2=server02:2888:3888
server.3=server03:2888:3888

## Zookeeper/data 내에 myid 생성 및 서버별 숫자 지정
cd zookeeper/data
myid -> 1

myid -> 2

myid -> 3

echo '1' > myid

## 다운받은 주키퍼를 Server02,03에 내려주고 각 서버내에서 소프트링크 생성
scp apache-zookeeper-3.5.9-bin.tar.gz server02:/home/hadoop/

ssh server02
tar xvfz apache-zookeeper-3.5.9-bin.tar.gz 
ln -s apache-zookeeper-3.5.9-bin zookeeper

scp apache-zookeeper-3.5.9-bin.tar.gz server03:/home/hadoop/
tar xvfz apache-zookeeper-3.5.9-bin.tar.gz 
ln -s apache-zookeeper-3.5.9-bin zookeeper

## Zookeeper 디렉토리내 수정사항을 Server02,03에 내려주고 각 서버내에서 myid 수정
cd zookeeper
scp -r * server02:/home/hadoop/zookeeper/
scp -r * server03:/home/hadoop/zookeeper/

ssh server02
cd zookeeper/data
nano myid -> 2

ssh server03
cd zookeeper/data
nano myid -> 3

## 주키퍼 서버 실행 및 스테이터스 확인
bin/zkServer.sh start
bin/zkServer.sh status

server01
bin/zkCli.sh

server02
bin/zkCli.sh

## KAFKA 다운로드, 압축해제 및 소프트링크 설정
wget (kafka URL)
tar -xzf kafka_2.13-2.6.3.tgz
ln -s kafka_2.13-2.6.3 kafka

## Zookeeper 정지
server01, server02, server03
bin/zkServer.sh stop

## KAFKA config/zookeeper.properties 수정 
server01
cd kafka
cd config

cd kafka
cd libs
cd ../config
cat zookeeper.properties

## bin/kafka-topics.sh 실행
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic Hello

bin/kafka-topics.sh --list --zookeeper localhost:2181

## Console-Producer,Consumer 설정
bin/kafka-console-producer.sh --broker-list server92 --topic Hello

bin/kafka-console-consumer.sh --bootstrap-server server01:9092 --topic Hello

## myenv 실행 후 kafka-python 다운로드
kafka-python
source ~/myenv/bin/activate
pip3 install kafka-python

## kafka 실습용.. 주피터 노트북 실행 후 localhost:8888진입 후 작성함
from kafka import KafkaProducer
from kafka.errors import KafkaError
from json import dumps
import time

producer = KafkaProducer(bootstrap_servers=['server01:9092'])

producer = KafkaProducer(value_serializer=lambda m: dumps(m).encode('utf-8'))
start = time.time()
for i in range(10000):
    data = {'name' : 'data' + str(i)}
    producer.send('Hello', data)
    producer.flush()
print("end time :", time.time() - start)

## kafka spark  hadoop 작업방식
kafka, spark, hadoop(hdfs) => 

source1(mysql) -> producer -> kafka1 -> consumer -> spark -> mysql..-> ..visual 
source2(stream) -> producer -> kafka2 -> consumer -> spark streaming -> mysql..

webservice service -> deploy
kafka-python ...
kafka-connect...

## kafka, zookeeper 정지
bin/kafka-server-stop.sh
bin/zookeeper-server-stop.sh

server01 , server02, server03
cd kafka
mkdir data
cd data
echo '1' > myid

cd ../config
nano zookeeper.properties
tickTime=2000
initLimit=10
syncLimit=5
maxClientCnxns=0
dataDir=/home/hadoop/kafka/data
clientPort=2181
server.1=server01:2888:3888
server.2=server02:2888:3888
server.3=server03:2888:3888

nano server.properties
broker.id = 1
listeners=PLAINTEXT://:9092
advertised.listeners=PLAINTEXT://:9092

scp -r kafka_2.13-2.6.3 server02:~/
ln -s kafka_2.13-2.6.3 kafka

zookeeper.connect=server01:2181,server02:2181,server03:2181