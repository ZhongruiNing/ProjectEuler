num = []
for a in range(2, 101):
    for b in range(2, 101):
        temp = a ** b
        if temp not in num:
            num.append(temp)

print(len(num))
