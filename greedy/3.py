# 1이 될 때까지 (99p)
# 이것도 쉬웠음

N, K = map(int, input().split())

cnt = 0
while N != 1:
    if N%K == 0:
        N = N//K
        cnt += 1
    else:
        N = N-2
        cnt += 1

print(cnt)