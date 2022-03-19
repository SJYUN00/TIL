## 함수부
def  add_data(friend) : # 선형 리스트에 추가
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def  insert_data(position, friend) :
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position) :
    katok[position] = None
    kLen = len(katok)
    for i in range(position+1, kLen, 1) :
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

## 전역변수부
katok = [] # 선형 리스트

## 메인코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)
delete_data(4)
print(katok)