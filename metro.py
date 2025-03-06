a = input().strip().split()
b = input().strip().split()
a = list(map(int, a))
b = list(map(int, b))
s= 0
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] == b[i]==1:
            s += 1
    print(s)
