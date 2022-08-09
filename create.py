import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database = 'emp1')

cursor = con.cursor()


while True:
    # name & age ask from user and try to insert it to database .
    name = input("Enter the name")
    age =  int(input("age batao bhai"))

    query = "insert into user values ('{}',{} )".format(name,age)
    cursor.execute(query)
    con.commit()

    print("Data enetered successfully!!")

    choice = input("2.Exit")
    if choice == '2':
        break


