try: 
 num1 = int(input("Enter first number: "))
 num2 = int(input("Enter the second number: "))
 result = num1 / num2
 print("The result is: ", result)
except ZeroDivisionError:
 print("Division by zero is an error")
except ValueError:
 print("Please enter a valid digit")
except:
 print("Incorrect input")
else:
 print("No exceptions")
finally:
 print("This will always execute no matter what.")