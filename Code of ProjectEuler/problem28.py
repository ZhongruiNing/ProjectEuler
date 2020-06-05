import numpy as np

# 定义矩阵大小
length = 1001

# 初始化矩阵
a = np.zeros([length, length])

# 定义右上角
ini = length ** 2
a[0][length - 1] = ini

# 定义方向，1左2下3右4上
direction = 1

# 定义迭代长度
number = [length]
for i in range(length, 1, -1):
    number.append(i)
    number.append(i)

# 定义第几个步骤
step = len(number)

# 定义起始点横纵坐标：
start_heng = 0
start_zong = length - 1

# 为矩阵赋值
for j in range(step):
    if direction == 1:
        for i in range(number[j]):
            a[start_heng][start_zong - i] = ini - i
        start_heng = start_heng
        start_zong -= i
        ini = ini - i
        direction = 2
        continue
    if direction == 2:
        for i in range(number[j]):
            a[start_heng + i][start_zong] = ini - i
        start_heng += i
        start_zong = start_zong
        ini -= i
        direction = 3
        continue
    if direction == 3:
        for i in range(number[j]):
            a[start_heng][start_zong + i] = ini - i
        start_heng = start_heng
        start_zong += i
        ini -= i
        direction = 4
        continue
    if direction == 4:
        for i in range(number[j]):
            a[start_heng - i][start_zong] = ini - i
        start_heng -= i
        start_zong = start_zong
        ini -= i
        direction = 1
        continue

r_t_l = np.diag(np.fliplr(a))
l_t_r = np.diagonal(a)

print(l_t_r.sum() + r_t_l.sum() - 1)
