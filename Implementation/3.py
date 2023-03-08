# 나 왜 이렇게 잘하지,,
o = input()

options = [(2, 1), (2, -1), (-2, 1), (-2, -1),
           (1, 2), (1, -2), (-1, 2), (-1, -2)]

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

col = dic[o[0]]
row = o[1]

cnt = 0
for i in options:
    if 9>col+i[0]>0 and 9>int(row)+i[1]>0:
        cnt+=1

print(cnt)