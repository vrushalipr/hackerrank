from itertools import combinations_with_replacement

io = input().split()
s = sorted(io[0])
k = int(io[1])

for i in combinations_with_replacement(s,k):
    print(''.join(i))
