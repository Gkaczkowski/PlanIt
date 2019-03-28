import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Gareth123!', db='BucketList')
cursor = conn.cursor()

select_query  = "select * from tbl_user"
cursor.execute(select_query)
records = cursor.fetchall()

for row in records:
       print("Member Number = ", row[0], )
       print("Name = ", row[1])
       print("Email  = ", row[2])
