import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="pythonsample"
)

c=conn.cursor()

if conn.is_connected():
    print("database is intilized successfully")
####
####c.execute("""create database pythonsample;
####            use pythonsample;
####          """)
print("database is created.")

##c.execute("""
##create table student(
##    regeno int primary key,
##    name varchar(20) not null,
##    age int
##);
##    """)
print("tabele is created")

regno=int(input("regno:"))
name=input("name")
age=int(input("age:"))
c.execute("""
insert into student values(%s,%s,%s); """, (regno,name,age))

conn.commit();
print("1 row is inserted")
c.execute("select *from student")
table=c.fetchall()
for i in table:
    print(i)
c.close()
