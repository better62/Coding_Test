N = int(input())

sub = 45*15 + 15*60
total = sub * N

if N >= 23:
    total += 59*59*3
elif N >= 13:
    total += 59*59*2
elif N >= 3:
    total += 60*60

print(total)
