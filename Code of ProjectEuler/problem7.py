from math import sqrt

def isprime(num):
    #flag=0，素数，flag=1，合数
    flag = 0
    if num == 1:
        flag = 1
        return flag
    if num == 2:
        return flag
    for i in range(2,int(sqrt(num))+1,1):
        if num % i == 0:
            flag = 1
            return flag
    return flag

i=1
count = 1
while i <= 10001:
    if isprime(count) == 0:
        i += 1
    count += 1
print(count-1)