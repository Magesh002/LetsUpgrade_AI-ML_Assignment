def minMax(dic):
    v = list(dic.values())

    mini = maxi = v[0]

    for i in v:
        if mini > i:
            mini = i
        elif maxi < i:
            maxi = i

    print("The min value is: ", mini, "\nThe max value is: ", maxi)


d = {'1': 1, '2': 5, '3': 3, '4': 2, '5': 21, '6': 4}
minMax(d)
