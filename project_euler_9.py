a = 0
c = 0
while a < 300:
    a = a + 1
    b = 0
    while b < 500:
        b = b + 1
        c = 1000-(a+b)
        if (a**2)+(b**2)==(c**2):
            print (a*b*c)

            break
        else :
            pass
