def calcu(num):
    result = 0
    for i in str(num):
        result += int(i) ** 5
    return result


result = 0
for i in range(2, 999999):
    if i == calcu(i):
        result += i
print(result)