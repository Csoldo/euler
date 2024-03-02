a = 1
b = 2
fib = 0

sum = 2
while fib < 4000000:
    fib = a + b
    a = b
    b = fib
    if fib % 2 == 0:
        sum += fib

print(sum)
