import numpy as np
factor = 2
num = 600851475143
while factor <= int(np.sqrt(num)):
    if num % factor == 0:
        num /= factor
    elif factor == 2:
        factor += 1
    else:
        factor += 2

print(num)