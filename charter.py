import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "yacht"
)
dcursor=conn.cursor()
for i in range (1,8):
    yacht_id = input("yacht_id:")
    startDate = input("startDate:")
    durationOfCharter = input("durationOfCharter:")
    user_id = input("user_id:")
    expectyedDateOfArrival= input("expectyedDateOfArrival:")
    durationOfStay = input("durationOfStay:")
    portId = input("portId")
    sql = "INSERT INTO charter (yacht_id,startDate,durationOfCharter,user_id,expectyedDateOfArrival,durationOfStay,portId) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values=(yacht_id,startDate,durationOfCharter,user_id,expectyedDateOfArrival,durationOfStay,portId)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM charter")
data = dcursor.fetchall()
for x in data:
    print(x)