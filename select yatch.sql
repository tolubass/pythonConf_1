import mysql.connector
conn=mysql.connector.connect(
    host= "localhost",
    username= "TRAIN",
    password= "train",
    database="tolu"
)
dcursor = conn.cursor()
sql="SELECT * FROM prop WHERE classes=%s OR scores=%s ORDER BY id ASC LIMIT 0,4"
para = ('ss1','23')
dcursor.execute(sql,para)
data = dcursor.fetchall()
for x in data:
    print(x)
l=len(data)
i=0
while i<l:
    a=input("Enter next/back:")
    if a=="next":
        sql = "SELECT * FROM prop WHERE classes=%s OR scores ORDER BY id ASC LIMIT 4,4"
        para = ('ss1',)
        dcursor.execute(sql, para)
        data = dcursor.fetchall()
        for p in data:
            print(p)

    elif a=="back":
        print(data)
        i+=1
    else:
        print("Error: unknown function")
        break



