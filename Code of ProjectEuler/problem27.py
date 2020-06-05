from math import sqrt


def isprime(num):
    # flag=1，素数，flag=0，合数
    flag = 1
    if num == 2:
        return flag
    for i in range(2, int(sqrt(num)) + 1, 1):
        if num % i == 0:
            flag = 0
            return flag
    return flag


result = 0
result_a = 0
result_b = 0
for a in range(0, 1000, 1):
    for b in range(0, 1000, 1):
        count = 0
        i = 0
        while (isprime(i ** 2 + a * i + b)):
            count += 1
            i += 1
        if count > result:
            result = count
            result_a = a
            result_b = b
for a in range(-1000, 0, 1):
    for b in range(int((a ** 2) / 4), 1000, 1):
        count = 0
        i = 0
        while (isprime(i ** 2 + a * i + b)):
            count += 1
            i += 1
        if count > result:
            result = count
            result_a = a
            result_b = b
print("result：" + str(result))
print("result_a：" + str(result_a))
print("result_b：" + str(result_b))
print("product：" + str(result_b * result_a))
