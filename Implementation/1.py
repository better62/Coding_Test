N = int(input())
steps = list(input().split())
o = [1, 1]

for i in steps:
    if i == 'L':
        if o[1] == 1:
            continue
        else:
            o[1] -= 1

    elif i == 'R':
        if o[1] == N:
            continue
        else:
            o[1] += 1

    elif i == 'U':
        if o[0] == 1:
            continue
        else:
            o[0] -= 1

    elif i == 'D':
        if o[0] == N:
            continue
        else:
            o[0] += 1


print(o[0], o[1])


