import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'emp1')

cursor = con.cursor()


name = input("Enter the name")


query = "delete from user where name = '{}'".format(name)
cursor.execute(query)
con.commit()
print("Data del successfully!!")