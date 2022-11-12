# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nl = list(input().split())
b = int(input())
bl = list(input().split())

s1 = set(nl)
s2 = set(bl)

print(len(s1.difference(s2)))
