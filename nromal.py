h=input("enter a number:")
i=input("enter another number:")
try:
    result=int(h)/int(i)
    print(f"the answer of this is:{result}")
except ZeroDivisionError as e:
    print(f"invalid input, pls check what you typed before you execute:")
except ValueError as p:
    print(f"invalid input, check the value very well!")
else:
    print(f"the result of the division is: {result}")
