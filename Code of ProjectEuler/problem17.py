"""如果数字 1 到 1000（包含 1000）用英文写出，那么一共需要多少个字母？"""

know = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4, '10': 3,
        '11': 6, '12': 6, '13': 8, '14': 8, '15': 7, '16': 7, '17': 9, '18': 8, '19': 8, '20': 6,
        '30': 6, '40': 5, '50': 5, '60': 5, '70': 7, '80': 6, '90': 6, '100': 10,
        '200': 10, '300': 12, '400': 11, '500': 11, '600': 10, '700': 12, '800': 12, '900': 11}

num = 0
for i in range(1, 1001):
    n = str(i)  # 字符串化
    if n in know:  # 已知直接加
        num += know[n]

    elif i > 20 and i < 100 and n not in know:  # 20到100且未在字典中
        num += know[n[0] + '0'] + know[n[1]]  # [0]几十的长度 + 个位的长度

    elif i > 100 and i < 1000:
        num += know[n[0]] + 10  # hundered and 总共是10个字母
        if str(int(n[1:3])) in know:
            num += know[str(int(n[1:3]))]  # 已知直接加
        else:
            num += know[n[1] + '0'] + know[n[2]]  # 未知再来算痛上一个elif

    else:  # One thousand 11个
        num += 11
print('答案是：' + str(num))