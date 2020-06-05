count = 0
a1=1
a2=2
temp = 2
while(a2 < 4000000):
    if temp % 2 == 0:
        count += a2
    temp = a1 + a2
    a1 = a2
    a2 = temp
print(count)