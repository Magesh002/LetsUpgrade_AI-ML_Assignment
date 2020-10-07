print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Floor Division\n6. Modulo\n")

opt = int(input("Select the option: "))

if opt < 5:
    c1 = complex(input("\nEnter first complex number: "))
    c2 = complex(input("Enter second complex number: "))
    if opt == 1:
        print("Addition of 2 complex number is:", c1 + c2)
    elif opt == 2:
        print("Subtraction of 2 complex number is:", c1 - c2)
    elif opt == 3:
        print("Multiplication of 2 complex number is:", c1 * c2)
    elif opt == 4:
        print("Division of 2 complex number is:", c1 / c2)
elif opt == 5:
    print("\nFloor division is not possible with complex number")
elif opt == 6:
    c = complex(input("\nEnter complex number: "))
    print("Modulo of the complex is derived from abs() function:", abs(c))
else:
    print("Invalid Option")