##함수
def openBox():
  global count
  count -= 1
  if count == 0:
    print('##반지넣기##')
    return
  openBox()
  print('상자 닫기!!!')
  return
##메인
count = 5
openBox()