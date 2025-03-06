def find_string(s, t, n):
    if len(s) > n:
        return "-1"
    candidate1 = s + 'a' * (n - len(s))
    if t not in candidate1:
        return candidate1
    candidate2 = 'a' * (n - len(s)) + s
    if t not in candidate2:
        return candidate2
    mid_index = (n - len(s)) // 2
    candidate3 = 'a' * mid_index + s + 'a' * (n - len(s) - mid_index)
    if t not in candidate3:
        return candidate3

    return "-1"
s = input().strip()
t = input().strip()
n = int(input())
print(find_string(s, t, n))
