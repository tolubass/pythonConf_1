import sql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tolu"
)

h1=input("name:")
h3=input("age:")
h4=input("phone_number:")
h5=input("email:")
h6=input("state_of_origin:")
h7=input("nationality:")

dcursor = conn.cursor()
sql = "INSERT INTO tolu (name,age,phone_number,email,state_of_origin,nationality) VALUES (%s,%s,%s,%s,%s,%s)"

values = (h1,h3,h4,h5,h6,h7)
dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + " was inserted")


