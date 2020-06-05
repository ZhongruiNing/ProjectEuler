from math import pow
def square_sum(num):
    sum = 0
    for i in range(1,num+1):
        sum += pow(i,2)
    return sum

def sum_square(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return pow(sum,2)

result = sum_square(100) - square_sum(100)
print(int(result))