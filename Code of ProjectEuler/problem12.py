from math import sqrt

def leijia(num):
    return (1+num)*num/2

def fenjie(num):
    result = []
    for i in range(1,int(sqrt(num)+1),1):
        if num % i == 0:
            result.append(i)
    return len(result)*2

divisions = 0

i=1
for weishu in range(1,1000,1):    
    while(divisions <= weishu):
        divisions = fenjie(leijia(i))
        if divisions >= weishu:
            result = leijia(i)
            break
        i=i+1
    print("超过"+str(weishu)+"位的第一个三角数是"+str(result)+"，因子共有"+str(divisions)+"位数，这是第"+str(i)+"个数")


