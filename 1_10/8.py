with open('in_8.txt') as f:
    lines = f.read().splitlines()
input = ""
for l in lines:
    input += l

max = 0
for i in range(1000-13):
    product = 1
    for j in range(i+1, i+14):
        product *= int(input[j])
    if max < product:
        max = product

print(max)
