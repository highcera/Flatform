import pymysql

# 전역변수 선언부
conn, curs = None, None
data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""
sql=""

# 메인 코드
conn = pymysql.connect(host="localhost", user="root", password="dark##2993", db="workbench", charset="utf8")
curs = conn.cursor()

while (True) :
    data1 = input("사용자 ID ==> ")
    if data1 == "" :
        break;
    data2 = input("사용자 이름 ==> ")
    data3 = input("사용자 이메일 ==> ")
    data4 = input("사용자 출생연도 ==> ")
    sql = "INSERT INTO user VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    curs.execute(sql)

conn.commit()
conn.close()
