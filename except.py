a = input("Enter a valid integer:")
b = input("Enter another valid integer:")
try:
    result = int(a) / int(b)
    print(f"The result of the division is: {result}")
except ZeroDivisionError as e:
    print("Invalid input! Your divisor becomes zero!")
    print(f"Error details:{e}")
except ValueError as k:
    print("Invalid input! Provide a correct input next time!")
    print(f"Error details: {k}")
print("The program completes successfully.")




