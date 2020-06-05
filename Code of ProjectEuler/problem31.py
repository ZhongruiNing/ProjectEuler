count = 0
for a in range(201):
    for b in range(201 - a):
        for c in range(201 - a - 2 * b):
            for d in range(201 - a - 2 * b - 5 * c):
                for e in range(201 - a - 2 * b - 5 * c - 10 * d):
                    for f in range(201 - a - 2 * b - 5 * c - 10 * d - 20 * e):
                        for g in range(201 - a - 2 * b - 5 * c - 10 * d - 20 * e - 50 * f):
                            for h in range(201 - a - 2 * b - 5 * c - 10 * d - 20 * e - 50 * f - 100 * g):
                                if a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h == 200:
                                    count += 1
                                    print("The " + str(count) + "th method is " + str(a) + " 1p + " +
                                          str(b) + " 2p + " + str(c) + " 5p + " +
                                          str(d) + " 10p + " + str(e) + " 20p + " +
                                          str(f) + " 50p + " + str(g) + " 100p + " +
                                          str(h) + " 200p ")

print("The totol number of the method is " + str(count))
