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