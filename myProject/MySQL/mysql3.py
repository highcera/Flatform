# Delete
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="dark##2993", db="workbench", charset="utf8")
try:
    curs = conn.cursor()
    sql = """delete from user where region=%s"""
    curs.execute(sql, '금산')
    conn.commit()

    sql2 = "select * from user order by no"
    curs.execute(sql2)
    rows = curs.fetchall()
    print(rows)
finally:
    conn.close()