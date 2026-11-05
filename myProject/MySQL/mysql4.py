import pymysql

# 전역변수 선언부
conn, curs = None, None
data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
row = None

# 메인 코드
conn = pymysql.connect(host="localhost", user="root", password="dark##2993", db="workbench", charset="utf8")
curs = conn.cursor()
sql = "select * from user"
curs.execute(sql)

print("No    ID     name    regin         insdt       upddt    ")
print("========================================================")

while (True):
    row = curs.fetchone()
    if row == None:
        break
    data1, data2, data3, data4, data5, data6 = row
    print("%5s %5s %10s %10s %10s %10s" % (data1, data2, data3, data4, data5, data6))

conn.close()