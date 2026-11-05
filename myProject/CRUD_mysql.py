# 코딩왕국

import pymysql

# connect
db = pymysql.connect(host="localhost", user="root", password="dark##2993",  charset="utf8")
curs = db.cursor(pymysql.cursors.DictCursor)

curs.execute('USE helloworld;')
# Insert
# curs.execute('INSERT INTO lang (name, description, study) VALUES ("Java", "Java is for programming", FALSE)')

# List
curs.execute('SELECT * FROM lang;')
value = curs.fetchall()
print(value)

# Update
# curs.execute('UPDATE lang SET description="HTML is for the form web" WHERE name="HTML"')

# Delete
# curs.execute('DELETE FROM lang WHERE name="Java"')

db.commit()
db.close()