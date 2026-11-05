import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pymysql
# import mysql.connector
import pandas as pd
import openpyxl


from_class = uic.loadUiType("C:/Flatform/myProject/Project_Template/editor.ui")[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__() # 부모클래스 생성자 실행
        self.setupUi(self)
        self.setWindowTitle("SQL MAKER!")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btnConnect.clicked.connect(self.connectDB)
        self.btnSee.clicked.connect(self.SeeTable)
        self.btnTable.clicked.connect(self.showTable)
        self.btnMkTable.clicked.connect(self.tableOpenFile)
        self.make_it.clicked.connect(self.make_table)
        self.btnDel.clicked.connect(self.del_table)
        self.btnInsert.clicked.connect(self.insert_data)
        self.progressBar.valueChanged.connect(self.printValue)
        self.btnAdvance.clicked.connect(self.Advance)
        self.btnSave.clicked.connect(self.Save)

        self.make_table_check = False

        self.login_check = False
        self.table_str = ""
        self.save = False
    
    def Save(self):
        if self.login_check == False:
            self.state_line.setText("Please Login first to continue")
            return
        if self.save == False:
            self.state_line_3.setText("enter sql code")
            return

        text, ok = QInputDialog.getText(self, 'insert File Name', 'File Name :')
        if ok and text:
            name = text
        else:
            return
        
        name = name + '.csv'
        self.df.to_csv('./' + name , index=False)
        self.state_line_3.setText("make a " + name )
        self.save = False
        


    def Advance(self):
        if self.login_check == False:
            self.state_line.setText("Please Login first to continue")
            return
        if self.table_str == "":
            self.state_line_3.setText("no selected table")
            return

        text, ok = QInputDialog.getText(self, 'insert MySQL code', 'mySQL code :')
        if ok and text:
            sql = text
        else:
            return


        while (self.show_table.rowCount() > 0):
            self.show_table.removeRow(0)

        try:
            columns_list = []
                # select * from table
            col_sql = sql.replace(" ", "")
            if col_sql.find("select*") != -1 or col_sql.find("SELECT*") != -1 : 
                self.cursor.execute("show columns from bye")
                result = self.cursor.fetchall()
                for row in result:
                    row[0].replace("(", "")
                    row[0].replace("'", "")
                    columns_list.append(row[0])
            else:
                col_sql = sql.split(" ")
                start = False
                col_str =""
                for i in range(len(col_sql)):
                    if start == True:
                        if col_sql[i] == 'from' or col_sql[i] == 'FROM':
                            break
                        else:
                            col_str += (col_sql[i])
                    else:
                        if col_sql[i] == "select" or col_sql[i] == 'SELECT':
                            start = True

                col_str = col_str.replace(" ", "")
                col_str = col_str.split(",")
                for i in range(len(col_str)):
                    columns_list.append(col_str[i])

        
            self.show_table.setColumnCount(len(columns_list))
            self.show_table.setHorizontalHeaderLabels(each for each in columns_list)
            self.save = True


            self.cursor.execute(sql)
            result1 = self.cursor.fetchall()
            self.df = pd.DataFrame(result1, columns = [columns_list])

            for i in range(len(result1)):
                row = self.show_table.rowCount()
                self.show_table.insertRow(row)
                for j in range(len(columns_list)):
                    self.show_table.setItem(row, j, QTableWidgetItem(str(result1[i][j])))
            
            self.state_line_3.setText("ok")
                
        
        except:
            if sql.find("union") != -1:
                self.state_line_3.setText("not support Union")
                return
            
            elif sql.find("join") != -1:
                self.state_line_3.setText("not support join")
                return

            else:
                self.state_line_3.setText("You have an error in your SQL syntax")
                return



        
    
    def printValue(self):
        pass
    

    def insert_data(self):
        if self.login_check == False:
            self.state_line.setText("Please Login first to continue")
            return

        sql_sea = "show tables"
        self.cursor.execute(sql_sea)
        result = self.cursor.fetchall()
        if len(result) == 0:
            self.textEdit.setText("No table in database")
            return


        items = []
        for result_iterator in result:
            items.append(result_iterator[0])

        item, ok = QInputDialog.getItem(self, 'QInputDialog - insert data',
                                            'table:', items, 0, False)

        if ok and item:
            stra = item
        else:
            return
        
        name = QFileDialog.getOpenFileName(self)[0]
        if name == "":
            return
        if name[-3:] == "csv":
            try:
                df = pd.DataFrame(pd.read_csv(name))
            except:
                df = pd.DataFrame(pd.read_csv(name, encoding='EUC-KR'))
            
        
        elif name[-4:] == "xlsx":
            try:
                df = pd.DataFrame(pd.read_excel(name))
            except:
                df = pd.DataFrame(pd.read_excel(name, encoding='EUC-KR'))
        
        else:
            self.textEdit.setText("you choice worng file \n csv, xlsx only")
            return

        df = df.fillna(0)
        x_count = df.shape[1]
        sql2 = "insert into " + stra + " values ("
        for i in range(x_count):
            sql2 = sql2 + " %s"
            if(i != x_count -1):
                sql2 = sql2 + ", "
        sql2 = sql2 + " );"    

        
        count = 0
        cal = 1
        max = 100

        try:
            for i, row in df.iterrows():
                self.cursor.execute(sql2, tuple(row))
                self.local.commit()
                count += 1
                if count >= len(df)/max * cal:
                    self.progressBar.setValue(cal)
                    cal += 1;
        except:
            self.textEdit.setText("you insert wrong dataFile \n please check your csv, xlsx file\n column's length or column's type")
            return

        self.progressBar.setValue(100)

        while (self.show_table.rowCount() > 0):
           self.show_table.removeRow(0)

        self.cursor.execute(" show columns from " + stra)

        columns_list = []
        result = self.cursor.fetchall()
        for row in result:
            row[0].replace("(", "")
            row[0].replace("'", "")
            columns_list.append(row[0])
    

        self.show_table.setColumnCount(len(columns_list))
        self.show_table.setHorizontalHeaderLabels(each for each in columns_list)
        self.cursor.execute("select *  from " + stra)

        result1 = self.cursor.fetchall()
        for i in range(len(result1)):
            row = self.show_table.rowCount()
            self.show_table.insertRow(row)
            for j in range(len(columns_list)):
                self.show_table.setItem(row, j, QTableWidgetItem(str(result1[i][j])))
        
        self.textEdit.setText(str(len(df)) +  " data insert complete ! \ntotal : " + str(len(result1)))
        
        

        
    def del_table(self):
        if self.login_check == False:
            self.state_line.setText("Please Login first to continue")
            return

        sql_sea = "show tables"
        self.cursor.execute(sql_sea)
        result = self.cursor.fetchall()

        if len(result) == 0:
            return

        items = []
        for result_iterator in self.result:
            items.append(result_iterator[0])

        item, ok = QInputDialog.getItem(self, 'QInputDialog - table',
                                            'table:', items, 0, False)

        if ok and item:
            stra = item

        else:
            return

        sql2 = "drop table " + stra
        self.cursor.execute(sql2)
        self.SeeTable()
        
        while (self.show_table.rowCount() > 0):
           self.show_table.removeRow(0)

        
    def make_table(self):
        if self.login_check == False:
            self.state_line.setText("Please Login first to continue")
            return
        
        if self.make_table_check == False:
            self.textEdit.setText("please push 'table 제작' button first!!")
            return

        try:
            self.cursor.execute(self.sql)
            #self.state_line_2.setText(" )
            self.textEdit.setText("success make table!! name : " + self.table_name)
            self.SeeTable()

            
        except:
            self.textEdit.setText(self.table_name + " is already exists")
            self.make_table_check = False
            return

        self.cursor.execute(" show columns from " + self.table_name)
        columns_list = []
        result = self.cursor.fetchall()
        for row in result:
            row[0].replace("(", "")
            row[0].replace("'", "")
            columns_list.append(row[0])
    
        self.show_table.setColumnCount(len(columns_list))
        self.show_table.setHorizontalHeaderLabels(each for each in columns_list)

        self.cursor.execute("select *  from " + self.table_name)

        result1 = self.cursor.fetchall()
        for i in range(len(result1)):
            row = self.show_table.rowCount()
            self.show_table.insertRow(row)
            for j in range(len(columns_list)):
                self.show_table.setItem(row, j, QTableWidgetItem(str(result1[i][j])))
            
        self.make_table_check = False



    def tableOpenFile(self):
        if self.login_check == False:
            self.state_line.setText("Please Login first to continue")
            return

        name = QFileDialog.getOpenFileName(self)[0]
        if name == "":
            return

        if name[-3:] == "csv":
            try:
                df = pd.DataFrame(pd.read_csv(name))
            except:
                df = pd.DataFrame(pd.read_csv(name, encoding='EUC-KR'))
            
        
        elif name[-4:] == "xlsx":
            try:
                df = pd.DataFrame(pd.read_excel(name))
            except:
                df = pd.DataFrame(pd.read_excel(name, encoding='EUC-KR'))

        else:
            self.textEdit.setText("you choice worng file \n csv, xlsx only")
            return

        df_list = df.columns.values.tolist()
        text, ok = QInputDialog.getText(self, 'make table', 'table name :')
        if ok and text:
            self.table_name = text
        else:
            return

        table_type_list = []
        df_type = pd.DataFrame(
                        {'int' : ['1'],
                         'float' : ['1.0'],
                         'date' : ['2022-11-07'],
                         'object' : ["string"]
                       }) 
        df_type = df_type.astype({'int':'int'})
        df_type = df_type.astype({'float':'float'})

        for each in range(len(df_list)):
            for i in range(len(df_type)):
                if df[df_list[each]].dtype == df_type['int'].dtype:
                    table_type_list.append("int")
                elif df[df_list[each]].dtype == df_type['float'].dtype:
                    table_type_list.append("float")
                elif df[df_list[each]].dtype == df_type['object'].dtype:
                    table_type_list.append("varchar(100)")
        
        self.sql = "create table " + self.table_name + "\n" + \
                "("

        for i in range(len(df_list)):
                    self.sql = self.sql +" `" + df_list[i] + "` " + table_type_list[i]
                    if(i != len(df_list)-1):
                        self.sql = self.sql + "," + "\n"
        self.sql = self.sql + " );"

        self.textEdit.setText("check sql code \n\n" + self.sql)

        self.make_table_check = True


    def connectDB(self):
        try:
            # host = self.Uhost_line.text()
            # user =  self.Uname_line.text()
            # password = self.Upassword_line.text()
            # database = self.Udatabase_line.text()
            # port = 3306
            conn = pymysql.connect(host="localhost", user="root", password="dark##2993", db="stock_db", charset="utf8")

            self.state_line.setText("YES!")
            # self.local = conn #self 쓰면 클래스내에서 사용가능
            self.cursor = conn.cursor()
            self.login_check = True
            print("OK")           
            self.SeeTable()
        except:
            self.state_line.setText("NO!")
            print("Fail")
    
    def SeeTable(self):
        if self.login_check == False:
            self.state_line.setText("Please Login first to continue")
            return

        sql_sea = "show tables"
        self.cursor.execute(sql_sea)
        self.result = self.cursor.fetchall()
        print(self.result)
        # self.conn.close()

        while (self.tableWidget.rowCount() > 0):
           self.tableWidget.removeRow(0)

        for result_iterator in self.result:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(result_iterator[0]))
        

    def showTable(self):
        if self.login_check == False:
            self.state_line.setText("Please Login first to continue")
            return

        sql_sea = "show tables"
        self.cursor.execute(sql_sea)
        result = self.cursor.fetchall()

        if len(result) == 0:
            return

        items = []
        for result_iterator in result:
            items.append(result_iterator[0])

        item, ok = QInputDialog.getItem(self, 'QInputDialog - table',
                                            'table:', items, 0, False)

        if ok and item:
            stra = item
            self.se_ta.setText(item)
        else:
            return
        
        self.table_str = stra;
        while (self.show_table.rowCount() > 0):
           self.show_table.removeRow(0)

        # select * from table
        self.cursor.execute(" show columns from " + stra)

        columns_list = []
        result = self.cursor.fetchall()
        for row in result:
            row[0].replace("(", "")
            row[0].replace("'", "")
            columns_list.append(row[0])
    

        self.show_table.setColumnCount(len(columns_list))
        self.show_table.setHorizontalHeaderLabels(each for each in columns_list)

        self.cursor.execute("select *  from " + stra)

        result1 = self.cursor.fetchall()
        for i in range(len(result1)):
            row = self.show_table.rowCount()
            self.show_table.insertRow(row)
            for j in range(len(columns_list)):
                self.show_table.setItem(row, j, QTableWidgetItem(str(result1[i][j])))

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindows = WindowClass()
    
    myWindows.show()
    
    sys.exit(app.exec_())
