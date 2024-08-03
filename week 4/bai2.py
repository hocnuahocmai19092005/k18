a = list()
b = list()
n = int(input())
for i in range(n):
    a.append(int(input()))
for i in range(n):
    b.append(int(input()))
kt = 'khong'
d = list()
A = list()
for i in range(n):
    if b.count(a[i]) != 0:
        kt = 'co'
        d.append(a[i])
    else:
        A.append(a[i])
print(kt)
print('ds sv dki ca 2 ban la :',d)
print('ds sv chi dki ban 1 la: ',A)