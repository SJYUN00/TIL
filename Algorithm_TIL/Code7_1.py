##함수

##전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

##메인

#enque

rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print('출구<--', queue, '<--입구')

#deque

front += 1
data = queue[front]
queue[front] = None
print('식사 손님 : 화사')

front += 1
data = queue[front]
queue[front] = None
print('식사 손님 : 솔라')

front += 1
data = queue[front]
queue[front] = None
print('식사 손님 : 문별')
print('출구<--', queue, '<--입구')