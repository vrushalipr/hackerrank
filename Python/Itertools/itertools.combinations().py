# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

ip = input().split()
s = ip[0]
k = int(ip[1])

for i in range(1, k+1):
    for j in combinations(sorted(s), i):
        print("".join(j))
