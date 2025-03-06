a = int(input())
if 1 <= a <= 1000:  
    numbers = " + ".join(str(i) for i in range(1, a + 1))
    total = a * (a + 1) // 2
    print(f"{numbers} = {total}")
else:
    print("عدد باید بین ۱ تا ۱۰۰ باشد.")
