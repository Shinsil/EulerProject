prime = []
i = 1
prime_sum = 0
prime_num = 0
number = 0
while i<2000000-1:
    i += 2
    j = 1
    while j<i:
        j = j + 1
        if j == i:
            prime_num = i
            prime_sum = prime_sum + i

        elif i%j ==0 :
            break
        else :
            pass


print(prime_sum+2)
