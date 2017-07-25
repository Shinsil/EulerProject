sum = 0
a = 1
b = 1
while b <= 4000000:
    c = a + b
    if b%2 == 0 :
        sum = sum + b
        a = b
        b = c

    else :
        a = b
        b = c

print(sum)
