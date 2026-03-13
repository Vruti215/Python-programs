# Program to demonstrate user-defined exception

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    
    print("You entered:", num)

except NegativeNumberError as e:
    print("User Defined Exception Occurred:", e)
