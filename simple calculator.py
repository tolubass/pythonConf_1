print("simple calculator")
usr_input1 = input("enter first_number")
first_number = float (usr_input1)
valid_operators = ["+", "-", "*", "/"]
if usr_opr in valid_operators:
    compute(first_number, usr_opr, second_number)
else:
    print("invalid operator. cannot compute the result.")
    print("=" *25)
    print("This is a simple calculator")
    print("it supports the following operations")
    print("i)Addition"
          "\nii)Subtraction"
          "\niii)Multiplication and "
          "\niv)Division.")
    print("=" *25)
    valid_operators = ["+", "-", "*", "/"]

    def Add_numbers(num1,num2):

        return num1 + num2
    def subtraction_numbers (num1,num2):
        return num1 - num2
    def multiply_numbers (num1,num2):
        return num1 * num2
    def compute(num1,operator, num2):
        result = 0
        if operator == '+':
            result = add_numbers(num1,num2)
        elif operator == '-':
            result = subtraction_numbers(num1, num2)
        elif operator =='*':
            result = multiply_numbers(num1, num2)
        else:
            result = divide_numbers (num1, num2)
            print(f"teh first result is: {result}")
        def main():
            usr_input1=input("enter the first number:")
            first_number = float(usr_input1)
            user_input2 = input("enter the next number:")
            second_number = float(usr_input2)
            usr_opr = input("enter the oprator (+,-,*,/):")
            if usr_opr in valid_operators:
                compute(first_number, usr_opr, second_number)
            else:
                print("invalid operator: it cannot compute result")
            main()
