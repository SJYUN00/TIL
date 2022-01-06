##이진검색

import random

##함수
def binSearch():
  pos = -1
  start = 0
  end = len(ary) - 1
  while start <= end:
    mid = (start + end) // 2
    if fData == ary[mid]:
      return mid
    elif fData > ary[mid]:
      start = mid + 1
    else:
      end = mid - 1
  return pos
##전역
dataAry = [random.randint(1,999) for _ in range(20)]
findData =  dataAry[random.randint(0,19)]
dataAry.sort()

##메인
print('배열-->', dataAry)
position = binSearch(dataAry, findData)