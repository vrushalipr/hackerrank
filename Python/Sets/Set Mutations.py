# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
s = set(map(int, input().split()))
n = int(input())

for i in range(n):
    ip = input().split()
    if ip[0] == "intersection_update":
        temp = set(map(int, input().split()))
        s.intersection_update(temp)
    elif ip[0] == "update":
        temp = set(map(int, input().split()))
        s.update(temp)
    elif ip[0] == "symmetric_difference_update":
        temp = set(map(int, input().split()))
        s.symmetric_difference_update(temp)
    elif ip[0] == "difference_update":
        temp = set(map(int, input().split()))
        s.difference_update(temp)
    else:
        assert False
        
print(sum(s))
