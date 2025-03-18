n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    prev2, prev1 = 1, 3 
    for i in range(3, n + 1):
        curr = (3 * prev1 + 2 * prev2) % 10**9 + 7  
        prev2, prev1 = prev1, curr 
    print(prev1)