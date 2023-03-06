# 큰 수의 법칙 (92p)
# 이 문제 좀 잘 풀었다. O(N)으로 푼 것도 그렇고 풀이 방식도
# 반복되는 배열을 하나의 묶음으로 풀었음

N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data = sorted(data)

total = 0

tmp = M//(K+1)
tmp2 = M%(K+1)
sub_total = data[-1]*K + data[-2]

total = sub_total*tmp

for _ in range(tmp2):
    total += data[-1]

print(total)