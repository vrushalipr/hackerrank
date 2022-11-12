# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
el = list(input().split())
b = int(input())
bl = list(input().split())

a = set(el)
x = set(bl)

print(len(a.union(x)))
