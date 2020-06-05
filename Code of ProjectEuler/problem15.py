def jiecheng(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def zuheshu(n, m):
    return jiecheng(n) / (jiecheng(m) * jiecheng(n - m))


num = 0
path = 20
for i in range(path + 1):
    num += zuheshu(path, i) * zuheshu(path, path - i)
print(num)
