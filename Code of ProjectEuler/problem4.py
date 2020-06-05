def ishuiwen(num):
    #flag = 0 回文数
    #flag = 1 非回文数
    flag = 1
    str_yuan = str(num)
    str_fan = str_yuan[::-1]
    if str_fan == str_yuan:
        flag = 0
    return flag

result = 0
for i in range(100,1000,1):
    for j in range(i,1000,1):
        temp = i * j
        if ishuiwen(temp) == 0:
            if temp > result:
                result = temp
                resulti = i
                resultj = j
print(result)
print(resulti)
print(resultj)