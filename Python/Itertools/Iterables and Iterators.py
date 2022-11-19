from itertools import combinations

n = int(input())
a = input().split()
k = int(input())

count = 0
total = 0

for i in combinations(a, k):
    count += 'a' in i
    total += 1
print(count/total)
