import mysql.connector as connection
mydb = connection.connect(host = "localhost", user = "root", password = "27J@y@nth#45")
cursor = mydb.cursor()
#cursor.execute("create database student123")
cursor.execute("use student123")
#cursor.execute("create table Details(stud_id int(10), stud_name varchar(20), marks int(10))")
cursor.execute("insert into Details values(01,'Jayanth', 20), (02, 'Suresh', 20), (03, 'Naresh', 19), (04, 'Ramesh' , 19)")
mydb.commit()
cursor.execute("select * from Details ")
for i in cursor.fetchall() :
    print(i)

