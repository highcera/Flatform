import pymysql

conn = pymysql.connect(host="localhost", user="root", password="dark##2993", db="workbench", charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)
sql = "select * from user where region=%s"

curs.execute(sql, '대전')
rows = curs.fetchall()
# print(rows)

for row in rows:
    print(row)
    print(row['no'], row['id'], row['name']) # dictionary key값으로 data 접근

conn.close()
exit()