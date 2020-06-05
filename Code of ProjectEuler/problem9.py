from math import pow

def Pythagorean():
    for a in range(1,333,1):
        for b in range(1,int((1000-1)/2),1):
            c = 1000 - a - b
            if pow(a,2)+pow(b,2)==pow(c,2):
                result = [a,b,c]
                result_product = a*b*c
                return result , result_product

result,result_product = Pythagorean()
print(result)
print(result_product)