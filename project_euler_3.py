prime_factor = []
a = 0
i = 1
while i <=600851475143**0.5:
    i = i+2
    j = 1
    if 600851475143%i == 0:
        while j<=i :
            j = j+1
            if j == i:
                prime_factor.append(i)
                pass
            elif i%j == 0:
                break
            else :
                pass
    else :
        pass
print(prime_factor)
