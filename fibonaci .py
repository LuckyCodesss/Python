n1 = 0
n2 = 1
n = n1+n2
for x in range(0,8):
    n1 = n2
    n2 = n
    n = n1+n2
    print(n1)