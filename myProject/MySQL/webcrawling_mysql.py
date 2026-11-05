from bs4 import BeautifulSoup as bs
import urllib.request as req
import pymysql

url = "https://finance.naver.com/marketindex"

res = req.urlopen(url)
soup = bs(res, "html.parser", from_encoding = 'euc-kor')

name_nation = soup.select('h3.h_lst > span.blind')
name_price = soup.select('span.value')
print(name_price.value)


# connect
conn = pymysql.connect(host="localhost", user="root", password="dark##2993",  charset="utf8")
curs = conn.cursor(pymysql.cursors.DictCursor)

curs.execute('USE naverfinance;')