
def swap2Numbers(n1, n2):
    temp = n1
    n1 = n2
    n2 = temp
    return n1, n2


a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")

a, b = swap2Numbers(n1=a, n2=b)

print("The value of 1st number is:", a, "and the value of 2nd number is:", b)


