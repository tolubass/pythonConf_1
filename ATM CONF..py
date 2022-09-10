print('WELCOME TO VASDO MOBILE BANKING!')
#creating a backend start for a mobile banking app
restart=('Y')
print('='*35)
i=0
for i in range (1,4):
    pin = int(input("please enter your 4 digits pin:"))
    if pin == 1234:
        print("successful!!!")
        while restart not in ('no', 'NO', 'no', 'N'):
            balance = "10000"
            b1 = int(balance)
            print("your acct balance is")
            print(balance)

            a = "a. cash deposit"
            b = "b. transfer"
            c = "c. check balance"
            d = "d. change pin"
            e = "e. withdrawal"
            f = "f. cancel"
            print(a)
            print(b)
            print(c)
            print(d)
            print(e)
            print(f)
            r = input("ENTER YOUR OPERATION:")
            if r == "a":
                print("select range/amount")
                i = "i. 20,000-50,000"
                ii = "ii. 60,000-100,000"
                iii = "iii. 110,000-500,000"
                iv = "iv. 500,000 above..."
                v = "v. type your amount"
                print(i)
                print(ii)
                print(iii)
                print(iv)
                print(v)
                q = input("select your option:")
                if q == "i":
                    print("select c1/c2/c3/c4")
                    print("=" * 20)
                    c1 = "20000"
                    t1 = int(c1)
                    c2 = "30000"
                    t2 = int(c2)
                    c3 = "40000"
                    t3 = int(c3)
                    c4 = "50000"
                    t4 = int(c4)
                    print(c1)
                    print(c2)
                    print(c3)
                    print(c4)
                    amount = input("type c1/c2/c3/c4:")

                    if amount == "c1":
                        print("Transaction done successfully")
                        print("your new balance is")
                        print(b1 + t1)
                        restart=input("would you like to go back")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break
                    elif amount == "c2":
                        print("cash deposited successfully")
                        print("your new balance is")
                        print(b1 + t2)
                        restart = input("would you like to go back")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break
                    elif amount == "c3":
                        print("cash deposited successfully")
                        print("your new balance is")
                        print(b1 + t3)
                        restart = input("would you like to go back")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break
                    elif amount == "c4":
                        print("cash deposited successfully")
                        print("your new acct balance is")
                        print(b1 + t4)
                        restart = input("would you like to go back")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break
                    else:
                        print("invalid input!!!")
                elif q == "v":
                    print("please type the amount")
                    d1 = int(input("input amount:"))
                    print("your new balance is:")
                    print(d1 + b1)
                    break
                else:
                    print("invalid input!!!")
            elif r == "b":
                v1 = "transfer to first bank"
                v2 = "transfer to other bank"
                print("v1. transfer to first bank")
                print("v2. transfer to other bank")
                e = input("Enter v1/v2:")
                if e == "v1":
                    o = int(input("Enter amount you want to transfer:"))
                    if o > b1:
                        print("insufficient amount")
                        restart = input("would you like to go back")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break
                        elif o < b1:
                            print("transferred successfully!!!")
                            print("your new balance is")
                            print(b1 - o)
                            restart = input("would you like to go back")
                            if restart in ('n', 'NO', 'no', 'N'):
                                print("thank you")
                                break

                elif e == "v2":
                    print("note: charges is #10")
                    s1 = input("enter g to continue:")
                    if s1 == "g":
                        s2 = int(input("Enter amount you want to transfer:"))
                        if s2 > b1:
                            print("insufficient amount")
                            restart = input("would you like to go back")
                            if restart in ('n', 'NO', 'no', 'N'):
                                print("thank you")
                                break
                            elif s2 < b1:
                                print("transferred successfully!!!")
                                print("your new balance is")
                                print(b1 - s2 - 10)
                                restart = input("would you like to go back")
                                if restart in ('n', 'NO', 'no', 'N'):
                                    print("thank you")
                                    break
                            else:
                                print("invalid input!!!")

                    else:
                        print("invalid input!!!")

            elif r == "c":
                print("your balance is:")
                print(b1)
                restart = input("would you like to go back")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("thank you")
                    break

            elif r == "d":
                j1 = int(input("enter your former pin:"))
                j2 = int(input("enter your new pin:"))
                if j1 != j2:
                    print("pin changed successfully!!!")
                    restart = input("would you like to go back")
                    if restart in ('n', 'NO', 'no', 'N'):
                        print("thank you")
                        break
                else:
                    print("ERROR!!!\n pin must not be the same as the former pin")
                    by1 = int(input("enter your former pin:"))
                    by2 = int(input("enter your new pin:"))
                    if by1 != by2:
                        print("pin changed successfully!!!")

                    restart = input("would you like to go back")
                    if restart in ('n', 'NO', 'no', 'N'):
                        print("thank you")
                        break

            elif r == "e":
                ui = 1000
                p1 = int(input("type amount:"))
                for x in range(1, 1001):
                    if p1 < b1:
                        print("withdrawal successfully!!!")
                        print(f"your new balance is: {b1 - p1}")

                        restart = input("would you like to go back")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break

                    elif p1 > b1:

                        print("insufficient amount")
                        print("you can only withdraw amount less than in your balance")
                        restart = input("would you like to go back")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break

                    else:
                        print("invalid input!!!")
                        restart = input("would you like to go back")
                        if restart in ('n', 'NO', 'no', 'N'):
                            print("thank you")
                            break

            elif r == "f":
                print("THANKS FOR USING VASDO MOBILE BANKING!")
                restart = input("would you like to go back")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("thank you")
                    break
    else:
        print("incorrect pin: try again!!")







