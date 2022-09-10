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
    no_of_docking_places = input("no_of_docking_places:")
    start_date = input("start_date:")
    duration = input("duration:")
    date_of_arrival =input("date_of_arrival:")
    duration_of_stay = input("duration_of_stay:")
    sql = "INSERT INTO  charter3 (user_id,no_of_docking_places,start_date,duration,date_of_arrival,duration_of_stay) VALUES (%s,%s,%s,%s,%s,%s)"
    values=(user_id,no_of_docking_places,start_date,duration,date_of_arrival,duration_of_stay)
    dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")
dcursor.execute("SELECT * FROM charter3")
data = dcursor.fetchall()
for x in data:
    print(x)