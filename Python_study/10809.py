# S = input()

# S_char = list(map(str,S))


# 알파벳 리스트 인덱싱 리스트 X로

# alp = ord('a')
# X = []
# for i in range(26):
#   alpha = alp + i
#   X.append(alpha - 97)
# print(X)

# 입력받은 문자열 길이

# strlen = len(S)
# print(strlen)

# 문자열 인덱싱

# for i in S:
#   for j in range(i+1, strlen+1):
#     if i != strlen-1:
#       if S_char[0][i] == S_char[0][j]:
#        S_char[0][j] == 'A'
#        print(S_char)
#     elif i == strlen-1:
#       if S_char[0][i] == 'A':
#         break




  # print(alpha_list[4])
  # print(alpha-97, end=' ')

# a = 'a'
# A = int(ord(a))
# b = A + 1
# B = chr(b)
# print(B)
# ['a', 'd', 'c', , , 'e']


# Find 함수 이용
word = input()

for i in range(97,123):
  print(word.find(chr(i)))