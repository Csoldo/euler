num = 2520
divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

while True:
    all = True
    for d in divisors:
        if num % d != 0:
            all = False
            break
    if all:
        break
    num += 20

print(num)