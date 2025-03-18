t = int(input())
results = []
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    p = list(map(int, input().split()))
    best_sum = float('-inf')
    for i in range(n):
        best_sum = max(best_sum, b[i] + p[i])
    results.append(best_sum)
for result in results:
    print(result)
