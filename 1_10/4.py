def is_palindrome(x: str):
    return x == x[::-1]

max = 0
for i in range(1, 999):
    for j in range(1, 999):
        product = i * j 
        if is_palindrome(str(product)):
            if max < product:
                max = product

print(max)