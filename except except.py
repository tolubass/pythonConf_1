a=input("enter first number:")
b=input("enter second number:")
c=int(a)
d=int(b)
try:
    r=c/d
except Exception as e:
    print("An unknown error occurred.")
    print(f"Error details: {e}")
except ZeroDivisionError as e:
    print("Invalid input! Your divisor becomes zero!")
    print(f"Error details: {e}")
except ValueError as e:
    print("Invalid input! Provide a correct input next time!")
    print(f"Error details: {e}")
else:
    print(f"Result of the division is : {r}")





