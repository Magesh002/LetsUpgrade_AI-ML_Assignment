l = []
num = 2
while len(l) < 20:
    num = num + 1
    if num > 1:
        for i in range(2, num):
            if (num % 2 == 0) and ((num % i) == 0):
                break
        else:
            l.append(num)

print(l)
