def nthRootOfm(m, n=4):
    return pow(m, (1/n))


number = int(input("Enter the number: "))
print("The result is: ", nthRootOfm(m=number))