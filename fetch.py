import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'emp1')

cursor = con.cursor()

query = "select * from user"
cursor.execute(query)

# data = cursor.fetchone()
# data1 = cursor.fetchmany(2)
data2 = cursor.fetchall()
print(data2)