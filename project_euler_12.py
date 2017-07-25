i = 100
tri_num = 0

while True:
    tri_num = i*(i+1)/2
    a = []
    for k in range(1,int(tri_num**0.5)):
        if tri_num%k == 0:
            a.append(k)
            a.append(tri_num/k)
            a.sort()

    if len(a) > 500:
        print(tri_num)
        break
    else :
        i += 1
