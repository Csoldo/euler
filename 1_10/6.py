def sum_of_squares(num):
    sum = 0
    for i in range(num):
        sum += i * i
    return sum

def square_of_sum(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum * sum

input = 101 #Exclusive
result = square_of_sum(input) - sum_of_squares(input)
print(result)