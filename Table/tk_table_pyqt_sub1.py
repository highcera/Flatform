# # https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/

# import sys
# from datetime import datetime
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import Qt
# import pandas as pd

# class Test:
#     def __init__(self):
#         self.data = self.read_data()
#         print(self.data)
       
#     def read_data(self):
#         self.df=pd.read_csv("C:/Flatform/Table/tips.csv")
#         # print(self.df)
#         return self.df
import tkinter as tk
from tkinter import ttk

class TreeviewExample:
    def __init__(self, master):
        self.master = master
        self.master.title("Treeview Example")
        
        # create treeview widget
        self.tree = ttk.Treeview(self.master)
        
        # define columns
        self.tree["columns"] = ("name", "age", "gender")
        
        # set column headings
        self.tree.heading("name", text="Name")
        self.tree.heading("age", text="Age")
        self.tree.heading("gender", text="Gender")
        
        # add data to treeview
        self.tree.insert("", "0", text="Person 1", values=("John", 30, "Male"))
        self.tree.insert("", "1", text="Person 2", values=("Jane", 25, "Female"))
        self.tree.insert("", "2", text="Person 3", values=("Jim", 40, "Male"))
        
        # pack treeview widget
        self.tree.pack()
        
if __name__ == '__main__':
    root = tk.Tk()
    app = TreeviewExample(root)
    root.mainloop()
