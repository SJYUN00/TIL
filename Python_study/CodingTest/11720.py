N = int(input())
a = input()


b = [list(map(int, a))]


sum = 0


for i in range(0,N):
   sum = sum + b[0][i]
print(sum)