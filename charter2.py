import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)
dcursor=conn.cursor()
for i in range (1,6):
    user_id = input("user_id:")
    type = input("type:")
    model = input("model:")
    home_port = input("home_port:")
    number_of_berths =input("number_of_berths:")
    cost= input("cost:")
    sql = "INSERT INTO  charter2 (user_id,type,model,home_port,number_of_berths,cost) VALUES (%s,%s,%s,%s,%s,%s)"
    values=(user_id,type,model,home_port,number_of_berths,cost)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM charter2")
data = dcursor.fetchall()
for x in data:
    print(x)