prime = []
i = 1
prime_num = 0
number = 0
while i<10000000000:
    i += 2
    j = 1
    if number == 10000:
        break
    else :
        while j<i:
            j = j + 1
            if j == i:
                prime_num = i
                number = number + 1
            elif i%j ==0 :
                break
            else :
                pass


print(prime_num)
