n = int(input())
s = set()
s = input().split()
a = sorted(list(map(int,s)))
m = int(input())
b = set()
sum = 0
for i in a:
    sum += i
    if sum > m:
        break
    b.add(i)
print(b)