import numpy as np

def is_sq_number(num):
    for i in range(1, int(np.sqrt(num) + 1)):
        if num % i == 0 and num / i == i:
            return True
    return False

# print(is_sq_number(100))
sum = 10
a = 3
c = 5
while sum != 1000 and a < 1000:
    for b in range(a+1, 1000-a):
        if a + b + c >= 1000:
            break
        if not is_sq_number(a * a + b * b):
            continue
        else:
            c = int(np.sqrt(a * a + b * b))
        sum = a + b + c
        product = a * b * c
    a += 1
    # print(f"a: {a}, b:{b}, c: {c}, sum: {sum}")

print(product)