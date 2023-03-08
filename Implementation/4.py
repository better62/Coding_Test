# 좀 어려웠다..

row, col = map(int, input().split())

a, b, c = map(int, input().split())

loc = []

for _ in range(row):
    tmp = list(map(int, input().split()))
    loc.append(tmp)

rotation = [[(-1, 0), (0, -1), (1, 0), (0, 1)],
            [(0, 1), (-1, 0), (0, -1), (1, 0)],
            [(1, 0), (0, 1), (-1, 0), (0, -1)],
            [(0, -1), (1, 0), (0, 1), (-1, 0)]]

visited = [[a, b]]
cnt = 1
rot = rotation[c]

while True:
    stop = 0
    for idx, r in enumerate(rot):
        aa = a+r[0]
        bb = b+r[1]
        cc = 3-idx
        if -1<aa<row and -1<bb<row:
            if loc[aa][bb] == 1:
                stop += 1
                continue
            else:
                if [aa, bb] not in visited:
                    visited.append([aa, bb])
                    a = aa
                    b = bb
                    c = cc
                    rot = rotation[c]
                    cnt += 1
                else:
                    stop += 1
                    continue
        else:
            stop += 1

    if stop == 4:
        aa = a + rotation[c][2][0]
        bb = b + rotation[c][2][1]
        if -1 < aa < row and -1 < bb < row:
            if loc[aa][bb] == 1:
                break
            else:
                a = aa
                b = bb

print(cnt)