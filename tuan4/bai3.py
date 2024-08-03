n,m = map(int,input().split())
d = list()
d = input().split()
d = list(map(int,d))
a = input().split()
b = input().split()
a = list(map(int,a))
b = list(map(int,b))
sum = 0
for i in range(n):
    if a.count(d[i]) != 0:
        sum += 1
    if b.count(d[i]) != 0:
        sum -= 1
print(sum)