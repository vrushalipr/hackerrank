n = int(input())
nl = list(input().split())
b = int(input())
bl = list(input().split())

s1 = set(nl)
s2 = set(bl)

print(len(s1.symmetric_difference(s2)))
