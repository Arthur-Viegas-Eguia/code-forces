n = input("")
n = int(n)
while n != 1:
    print(n)
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = 3 * n + 1
print(n)
    
