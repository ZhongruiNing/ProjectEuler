from math import sqrt
import numpy as np
import time
#判断素数
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

result = 0
#method 1
start = time.time()
for i in range(1,2000000,1):
    if not isprime(i):
        result += i
end = time.time()
print(result)
print("Method1：")
print(end-start)

#method 2
result = []
start = time.time()
for i in range(1,2000000,1):
    if not isprime(i):
        result.append(i)
end = time.time()
result = np.array(result)
print(result.sum)
print("Method2：")
print(end-start)