## 푸티 실행
푸티 IP에 18.182.177.124 입력 save 후 Auth 목록으로 진입
Browse 창에서 PPK 2번 키를 선택해주고 
Session 목록에서 다시 save 후 open 실행

ID는 lab23 으로 진입

## conda python3 실행

``conda activate python3``

## 주피터 노트북 페이지 생성
``nohup jupyter-notebook --ip=0.0.0.0 --no-browser --port=8923 &``
여기서 푸티는 꺼도 노트북은 작동한다!

여기까지하면 
(http://18.182.177.124:8923/)에 주피터 노트북이 생성된다.

nohup 명령어가 실행된채로 PUTTY에 다음 명령어를 입력한다.

``pip install nbconvert==5.4.1``
이제 파일생성 기능을 사용할 수 있게 되었다.



