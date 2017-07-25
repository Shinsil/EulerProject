sum_square = 0
square_sum = 0
j = 0
result = 0
for i in range(1,101):
    j = i**2
    sum_square = sum_square + j

for k in range(1,101):
    square_sum = square_sum + k

result = (square_sum**2) - sum_square
print(result)
