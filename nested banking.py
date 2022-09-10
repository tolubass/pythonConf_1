print("welcome to iron bank")
restart=("Y")
chances=3
balance= 67.14
while chances >= 0:
    pin=int(input("please enter your 4 digits pin"))
    if pin==(1234):
        print("you entered your pin correctly\n")
        while restart not in ('no', 'NO', 'no', 'N'):

            print("please press 1 for your balance\n")
            print("please press 2 to make withdrawal\n")
            print("please press 3 to pay in\n")
            print("please press 4 to return card\n")
            option = int(input ("what would you like to choose?"))
            if option ==1:
                print( balance)
                restart=input("would you like to go back")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("thank you")
                    break
                elif option==2:
                    option2 = ('y')
                    withdrawl = float(input("how much would you like to withdraw?"))
                    if withdrawl in [10,20,40,60,80,100]:
                        balance=balance-withdrawl
                        print(balance)
                        restart = input("would you like to go back?")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break
                    elif withdrawl!=[10,20,40,60,80,100]:
                        print('invalid amount please re try\n')
                        restart = ('y')
                    elif withdrawl==1:
                        withdrawl=float(input('please enter desired amount:'))
                elif option==3:
                    pay_in=float(input('how much would you like to pay in?'))
                    balance=balance + pay_in
                    print(balance)
                    restart=input("would ypu like to go back?")
                    if restart in ('n', 'NO', 'no', 'N'):
                        print("thank you")
                    break
                elif option==4:
                    print('please wait while your card is returned ')
                    print("thank you for your service")
                    break
                else:
                    print("please enter a correct number")
                    restart =("y")
    elif pin!=("1234"):
        print("incorrect password")
        chances = chances -1
        if chances ==0:
            print('\nNo more tries')
            break