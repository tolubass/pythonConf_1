def operation(inp):
    answer = 0
    if inp.find ("+") !=-1:
        item=inp.split ("+")
        answer=int(eval(item[0])) + int(eval(item[1]))
    elif inp.find ("-") !=-1:
        item=inp.split ("-")
        answer=int(eval(item[0])) - int(eval(item[1]))
    elif inp.find("x") !=-1:
        item = inp.split("x")
        answer=int(eval(item[0])) * int(eval(item[1]))
    elif inp.find ("/") !=-1:
        item = inp.split ("/")
        answer = int(eval(item[0])) / int(eval(item[1]))
    return answer
a = input("operation:")
print (operation(a))


