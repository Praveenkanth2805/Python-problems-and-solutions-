from database_connector import db_connect

conn=db_connect()
c=conn.cursor()

c.execute("select *from student")
row=c.fetchall()
for i in row:
    print(i)

