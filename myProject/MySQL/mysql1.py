# insert

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="dark##2993", db="workbench", charset="utf8")
curs = conn.cursor()
# sql = """insert into user(id, name, region, insdt)
#         values (%s, %s, %s, now())"""
# curs.execute(sql, ('test10', '테스트10', '천안'))
# curs.execute(sql, ('test11', '테스트11', '아산'))
# curs.execute(sql, ('test12', '테스트12', '금산'))
# conn.commit()

sql2 = "select * from user order by no"
curs.execute(sql2)
rows = curs.fetchall()
print(rows)
conn.close()
exit()

# for row in rows:
#     print(row)
#     print(row['no'], row['id'], row['name']) # dictionary key값으로 data 접근