def func(num):
    if num % 2 == 0:
        return int(num/2)
    else:
        return int(3 * num + 1)

result = 0
result_number = 0
for i in range (1,1000000):
    jishu = 1
    num = i
    while (num != 1):
        jishu += 1
        num = func(num)
    if jishu > result:
        result = jishu
        result_number = i
    print("number " + str(i) + " contains " + str(jishu) + " numbers")

print("The number " + str(result_number) + " contains the longest chain, It has " + str(result) + "terms")