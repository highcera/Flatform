# update

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="dark##2993", db="workbench", charset="utf8")
curs = conn.cursor()
sql = """update user set insdt=now() where no <= 5"""
curs.execute(sql)
conn.commit()

sql2 = "select * from user order by no"
curs.execute(sql2)
rows = curs.fetchall()
print(rows)
conn.close()
exit()

# for row in rows:
#     print(row)
#     print(row['no'], row['id'], row['name']) # dictionary key값으로 data 접근