import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'emp1')

cursor = con.cursor()


name = input("Enter the name")
age = int(input("Enter the age"))


query = "update user set age = {} where name = '{}'".format(age,name)

cursor.execute(query)
con.commit()

print("Data updated!!")

