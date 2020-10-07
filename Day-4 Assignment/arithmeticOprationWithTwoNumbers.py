n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))

r = n1 - n2

if r > 25:
    print("Subtraction of two numbers", r, "is greater than 25.0, So the multiplication result is:", n1*n2)

else:
    print("Subtraction of two numbers", r, "is less than 25.0, So the division result is:", n1/n2)