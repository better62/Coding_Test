# 숫자 카드 게임 (96p)
# 쉬웠음
N, M = map(int, input().split())
min_list = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    min_list.append(min(tmp))

print(max(min_list))

