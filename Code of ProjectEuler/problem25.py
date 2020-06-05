def Fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        Fibo.append(Fibo[-1] + Fibo[-2])
        return Fibo[-1]


def length(num):
    return len(str(num))

Fibo = [1, 1]
i = 1
threshold = 1000
while True:
    if length(Fibonacci(i)) >= threshold:
        print(str(i) + " is the first term to contain " + str(threshold) + " digits")
        break
    else:
        i += 1