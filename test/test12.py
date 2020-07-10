#Python MySQL - mysql-connector 驱动
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    db="testdb",
    charset='utf8'
)
mycursor = mydb.cursor()

def findlist(sql):
    mycursor.execute(sql)
    listresult = mycursor.fetchall()
    return listresult

sql = "select * from userinfo order by uid"
for l in findlist(sql):
     print(l)
     for v in l:
         print(v)