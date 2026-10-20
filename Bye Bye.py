valid = False
while not valid:
    try:
        m = int(input("Enter a number: "))
        while m % 2 == 0:
            print("bye")
            m = int(input("Enter a number: "))
            valid = True
    except ValueError:
        print("Invalid")