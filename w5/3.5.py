import random
n = int(input('So sv la: '))
list = ['CNTT', 'KHMT', 'KTPM', 'HTTT']
msv = [input() for i in range(n)]
for i in range(n):
    d = {f"Account{i+1}" :
        {"Username" : msv[i] ,
         "Password" : random.choice(list) + msv[i] }
    }
    print(d)