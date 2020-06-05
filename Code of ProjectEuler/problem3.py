from math import sqrt

result=[]
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

#def qiuyinzi(num):
#    for i in range(2 , num + 1 , 1):
#        if isprime(i) == 0 and num % i == 0:
#            return i


num = 600851475143
#if isprime(num) == 0:
#    print("该数为素数")
#else:
#    i=1
#    while(num != 1):
#        i = qiuyinzi(num)
#        result.append(i)
#        num = int(num / i)
#print(result)

for i in range(2,int(sqrt(num))+1,1):
    if isprime(i) == 0:
        if num % i == 0:
            result.append(i)
print(result)
