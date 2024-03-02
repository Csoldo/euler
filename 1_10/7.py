import numpy as np

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

cnt = 1
i = 1

while cnt < 10001:
    i += 2
    if is_prime(i):
        cnt += 1

print(i)