h=input("do you want to change your password? enter yes/no:")
for i in range (1):
    if h=="yes":
        print("proceed")
    else:
        print("odabo")
        break
#set password from settings
#setting password as phone default
print("note: password must not be more than 5 digits")
set_password=int(input("Type your old password:"))
set_new_password=int(input("set new password:"))
confirm_password=int(input("confirm password:"))
if set_password==confirm_password:
    print("password must not be the same as old password")
elif set_password!=set_new_password:
    print("password changed successfully")
else:
    print("incorrect pin: try again!!!")

k=input("do you want to unlock your phone? yes/no")









