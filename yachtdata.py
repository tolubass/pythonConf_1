import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "yacht"
)
dcursor=conn.cursor()
for i in range (1,7):
    name = input("name:")
    type = input("type:")
    model = input("model:")
    homePort = input("homePort:")
    noOfBerth= input("noOfBerth:")
    cost = input("cost:")
    sql = "INSERT INTO  yachtdata (name,type,model,homePort,noOfBerth,cost) VALUES (%s,%s,%s,%s,%s,%s)"
    values=(name,type,model,homePort,noOfBerth,cost)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM yachtdata")
data = dcursor.fetchall()
for x in data:
    print(x)