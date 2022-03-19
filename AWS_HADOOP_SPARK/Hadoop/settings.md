## Virtual Box setting
새로만들기
이름 정하고 2048 MB 메모리
- 가이드모드가 아닌 전문가모드로 진입.
- 설정 > 저장소 에서 iso 파일을 등록해준다.
- 설정 > 네트워크 에서 NAT네트워크로 변경 후 미리 등록해두었던 MyDsNetwork를 선택 후 실행.
- 언어 설정후 done.
- user name을 hadoop으로 설정 후 192.168.10.0/24
- 192.168.10.101(102,103) 서버에 따라 뒷자리 변경
- 192.168.10.1
- 163.98. 설정 후 done
-    ?
- 재설정 필요



## * Hadoop 3.3.1(2.x...)
Core Functions
- HDFS (NameNode, DataNode)
- YARN (ResourceManager, NodeManager)
- Batch Processing (MapReduce) -> Java -> jar

server01 192.168.10.100 NameNode, ResourceManager, JVM
server02 192.168.10.101 DataNode, NodeManager, JVM
server03 192.168.10.102 DataNode, NodeManager, JVM

MyNetwork : 192.168.10.0/24
            192.168.10.0 ~ 255
Route : 192.168.10.1
DNS : 168.126.63.1

VirtualBox
=> single => NameNode, DataNode, ResourceManager, NodeManager

## ServerBase 계정
id : hadoop
pw : 1234

``ifconfig``

inet 192.168.10.100 이어야함

``sudo apt-get update``

ip chage -> 192.168.10.100
hostname change -> server01
hosts change(DNS) -> ....
java installed

``cd /etc/``
``cat /etc/hostname``
``sudo nano /etc/hostname``

``cat /etc/hosts``
``sudo nano /etc/hosts``
127.0.1.1 삭제
localhost는 냅두고 아래 서버 다 지우고 server01부터 03까지 적어줌

``ping hosts``로 확인

``reboot``

host(mypc) - > guest

localhost:13100 -> 192.168.10.100:22

``cd /usr/local``
``sudo mv jdk1.8.0_311/ /usr/local``
``sudo chown -R root:root jdk1.8.0_311/``
``sudo ln -s jdk1.8.0_311/ java``


``vi .profile`` 맨 밑에 추가
  export JAVA_HOME=/usr/local/java
  export HADOOP_HOME=/home/hadoop/hadoop
  export PATH=$PATH:$JAVA_HOME/bin
  export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/bin:$JAVA_HOME/lib/tools.jar
  export HADOOP_MAPRED_HOME=$HADOOP_HOME
  export HADOOP_COMMON_HOME=$HADOOP_HOME
  export HADOOP_HDFS_HOME=$HADOOP_HOME
  export HADOOP_YARN_HOME=$HADOOP_HOME
  export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
  export HADOOP_LOG_DIR=$HADOOP_HOME/logs
  export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
  export HADOOP_OPTS="-Djava.library.path=$HADOOP_COMMON_LIB_NATIVE_DIR"
  export HADOOP_PID_DIR=${HADOOP_HOME}/pids
  export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin:
  export CLASSPATH=$CLASSPATH:$HADOOP_HOME/lib/*
  export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

cat .profile 로 확인
source .profile

``wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.2/hadoop-3.3.2.tar.gz``로 하둡 설치

``tar xvfz hadoop-3.3.2.tar.gz`` 로 압축해제

``cd ~/hadoop/etc/hadoop``
``vi hadoop-env.sh``에서
``export JAVA_HOME=/usr/java/``
cd ~/hadoop에서 설정할 부분
  $ mkdir input
  $ cp etc/hadoop/*.xml input
  $ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.2.jar grep input output 'dfs[a-z.]+'
  $ cat output/*



## 2일차 하둡 활용 


하둡 설치 설정 가이드
https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html 

1. putty 로그인
ifconfig
java -version
javac -version
which java

rm -rf input
rm -rf output
mkdir input
cd input
touch mydata.txt

2. dfs로 시작하는 문자열 탐색
  
``bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.2.jar grep input output 'dfs[a-z.]+'``


3. 설정상 바꿔야하는 파일

etc/hadoop/core-site.xml:

<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>

etc/hadoop/hdfs-site.xml:

<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>

etc/hadoop/mapred-site.xml:

<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
</configuration>

etc/hadoop/yarn-site.xml:

<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>

4. ssh localhost 패스워드 없이 진입하기 위해
   
   ``ssh localhost``입력 후 yes

5. 키생성
  $ ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
  $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys  (overwrite가 아닌 append)
  $ chmod 0600 ~/.ssh/authorized_keys

6. 구동
   
home directory에서 
source .profile
cd hadoop
jps

``sbin/start-dfs.sh`` 로 시작

sudo systemctl status ufw
sudo systemctl stop ufw
sudo systemctl disable ufw (부팅시 자동시작 방지)



7. 디렉생성

bin/hdfs dfs -mkdir input
bin/hdfs dfs -put input/* input2
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.2.jar grep input output 'a[a-z.]+'

8. 포맷하기

sudo rm -rf /tmp/*
hdfs namenode -format


## 서버 복제하기

MAC주소 정책: 모든 네트워크 어댑터의 새 MAC주소생성 옵션 선택해야함 필수~!

## server01에서 셋팅한 xml파일을 server02,server03에 복사

``scp * server02:/home/hadoop/hadoop/etc/hadoop/`` 각 서버에 복사
``scp * server03:/home/hadoop/hadoop/etc/hadoop/``

``ssh server02 $JAVA_HOME:~/etc/jps`` 로 복사되었는지 확인.
``ssh server03 $JAVA_HOME:~/etc/jps``

stop-all.sh
start-all.sh