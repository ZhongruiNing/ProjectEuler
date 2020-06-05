from math import gcd
from math import sqrt

#minimum=1
#for i in range(1,11):
#    minimum = int(i) * int(minimum) / gcd(int(i), int(minimum))
#print(int(minimum))

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

#得到素数列表
def get_prime_list(num):
    prime_list=[]
    for i in range(2,num+1,1):
        if isprime(i) == 0:
            prime_list.append(i)
    return prime_list

#获取最小素数因子
def qiuyinzi(num):
    for i in range(2 , num + 1 , 1):
        if isprime(i) == 0 and num % i == 0:
            return i

num = 20
list = [i for i in range(2, num+1)]
prime_list = get_prime_list(num)
result = 1
for number in prime_list:
    list.remove(number)
    result *= number
for number in list:
    if result % number == 0:
        pass
    else:
        result *= qiuyinzi(number)
print(result)
    