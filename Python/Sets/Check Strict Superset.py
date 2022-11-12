a = set(input().split())
N = int(input())
output = True

for i in range(N):
    s = set(input().split())
    if not s.issubset(a):
        output = False
    if len(s) >= len(a):
        output = False

print(output)
