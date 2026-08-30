# Exception handling is used to handle errors
# without stopping the whole program.

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    # This runs if the user enters something
    # that cannot be converted into an integer.
    print("Please enter a valid number.")


# try and except can also be used with calculations

try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    # We cannot divide a number by zero.
    print("You cannot divide by zero.")


# else runs only when there is no error

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a number.")

else:
    print("Your age is:", age)


# finally runs whether there is an error or not

try:
    print("This is inside try.")

except:
    print("Something went wrong.")

finally:
    print("This will always run.")