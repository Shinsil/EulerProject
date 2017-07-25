prime_nums = [2,3,5]
def prime(num):
    for i in prime_nums:
        if i == 2 or i == 3:
            continue
        if i**2 > num:
            return True
        if num%i == 0:
            return False
    return True

j = 1
limit = 2000000

while True :
    a = 6*j + 1
    b = 6*j + 5

    if a> limit:
        break

    if prime(a) :
        prime_nums.append(a)

    if b > limit :
        break

    if prime(b):
        prime_nums.append(b)

    j = j+1

print(sum(prime_nums))
