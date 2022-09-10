import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "yacht"
)
dcursor=conn.cursor()
for i in range (1,8):
    phone  = input("Phone No:")

    expectyedDateOfArrival = input("expectyedDateOfArrival:")
    Departure = input("Departure:")
    sql = "SELECT yachtmmt.id FROM yachtmmt,users WHERE users.id=yachtmmt.user_id AND users.phoneNumber = %s ORDER BY yachtmmt.id DESC"
    para = (phone,)
    dcursor.execute(sql, para)
    data = dcursor.fetchone()
    if data[0] > 0 or data[0] !="":
        portId = input("portId:")
        yacht_id = input("yacht_id:")
        sql = "UPDATE yachtmmt SET portId = %s,yacht_id = %s WHERE id = %s"
        values = (portId, yacht_id, data[0])
        dcursor.execute(sql, values)
        conn.commit()
        print(str(dcursor.rowcount) + " was updated")
    else:
        sql = "INSERT INTO  yachtmmt ( user_id,portId,yacht_id,expectyedDateOfArrival, Departure) VALUES (%s,%s,%s,%s,%s)"
        values = (user_id, "", "", expectyedDateOfArrival, Departure)
        dcursor.execute(sql, values)
        conn.commit()
        print(str(dcursor.rowcount) + " was inserted")