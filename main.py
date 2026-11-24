try:
    number = int(input("Enter a number: "))
    print("Number is entered is ",number)

except ValueError as ex:
    print("Exception:", ex)