import numpy as np

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def sum_of_primes_below(num):
    cur = 3
    sum = 2
    while cur < num:
        if is_prime(cur):
            sum += cur
        cur += 2
    return sum

print(sum_of_primes_below(10))
print(sum_of_primes_below(2000000))