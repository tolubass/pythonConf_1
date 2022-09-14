sack = []
items = [30,20,30,25,10,5,6,5,10,10,8,15,15,15,15,15,10,14,16,24,8,22,2,22,22,22,22,22,22,10,10,10,10]

size = 200
total = 0
l = len(items)
i = 0
while i < l:
    sel = int(input("Enter Weight:"))
    cur = total + items[sel]
    message = ""
    if cur < size:
        total = total + items[sel]
        message = "Item added successfully"
        items.pop(sel)
    elif cur == size:
        total = total + items[sel]
        message = "Item added successfully, Bag is now full"
        items.pop(sel)
    elif cur > size:
        total = total
        message = "Item is too big to be added please..."
    h = str((total/size)*100.0)
    print(message + ". Bag is " + h + "% full")
    i += 1
