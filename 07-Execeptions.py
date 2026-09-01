# Exception handling helps us deal with errors
# without crashing the program.

try:
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    print("\nAddition:", first + second)
    print("Subtraction:", first - second)
    print("Multiplication:", first * second)
    print("Division:", first / second)
    print("Exponentiation:", first ** second)

except ValueError:
    # Runs when the user enters something
    # that is not a valid number.
    print("Please enter numbers only.")

except ZeroDivisionError:
    # Runs when the second number is 0.
    print("You cannot divide by zero.")

else:
    # Runs when there are no errors.
    print("Calculation completed successfully.")

finally:
    # This always runs at the end.
    print("Program finished.")