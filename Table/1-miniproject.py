all_records=[["박인덕", "010-1111-vvvv","aa","bb"], ["오수미", "010-2222-vvvv","cc","dd"],
          ["김인숙", "010-3333-vvvv","ee","ff"], ["최금혹", "010-4444-vvvv","gg","hh"],
          ["민동욱", "010-5555-vvvv","ii","jj"], ["성열휴", "010-6666-vvvv","kk","ll"],
          ["김동휘", "010-7777-vvvv","mm","nn"], ["이올석", "010-8888-vvvv","oo","zz"],
          ["김민규", "010-9999-vvvv","pp","qq"], ["홍길동", "010-1010-vvvv","rr","ss"],
          ["김민규", "010-1110-vvvv","tt","uu"]]   

from tkinter import *

def preparation():
    global pData, point
    pData = all_records
    point=0
    win.title('전화번호관리')
    setting_gui()
    setting_list()
    
def setting_list():
    for record in all_records:
         lst.insert(END,str(record[0] + ' ::  ' +record[1]))
    lst.focus_set()
    lst.selection_set(point)
    show_data(pData[point])
    
def on_select(event):
    id_list = event.widget
    selection_id = id_list.curselection()[0]
#    name = id_list.get(selection_id)
    data = pData[selection_id]
    print(data)
    show_data(data)

def show_data(data):
    for i in range(len(tx)):
        tx[i].delete(0, END)
        tx[i].insert(0, data[i])

def on_delete():
    ln=len(pData)
    if ln >= 1:
        point = lst.curselection()[0]

        pData.remove(pData[point])
        lst.delete(point)



        if point>=ln-1 :
            point=point-1

        if point >= 0: 
            data=pData[point]
            lst.selection_set(point)
        else:
            data = "","","",""
            print(point)
        show_data(data)            
        
def on_close():
    win.destroy()
    
def on_search():
    
    sName= tsearch.get()
    found=False
    for i in range(len(pData)):
       
        if sName in pData[i]:
           p= i
           found=True
           break
    if found:
        show_data(pData[p])

        lst.selection_clear(lst.curselection())
        lst.selection_set(p)
        lst.see(p)
                  
           
def on_update():
    ln=len(pData)
    if ln >= 1:
        point = lst.curselection()[0]
        lst.delete(point)
    else:
        point = 0
        pData.append(["","","",""])  #빈 리스트이므로 자리확보(인덱싱에러방지)

    for i in range(len(tx)):
        pData[point][i] = tx[i].get()

    lst.insert(point, tx[0].get() + " :: " + tx[1].get())
    lst.selection_set(point)
    lst.see(point) 
    for i in pData:
         print( i)
def on_add():
    pData.append([tx[0].get(),tx[1].get(),tx[2].get(),tx[3].get()])
    lst.insert(END, tx[0].get() + " :: " + tx[1].get())
    point= len(pData)-1
    lst.selection_clear(lst.curselection())
    lst.selection_set(point)    
    lst.see(point) 
    for i in pData:
         print( i)
def setting_gui():
    global lst, tx, pData, tsearch
      #레이블 세팅
    titles=('이       름: ','전 화 번 호: ','주       소: ', 'Email: ')
    for i in range(4):
        lbl=Label(win, padx = 20,text= titles[i])
        lbl.grid(row = i*2, column = 0,  sticky = 'nw')
    lbl_user = Label(win,padx = 20, text = '이   름 / 전화번호 ')
    lbl_user.grid(row = 0, column = 2, sticky = 'nw')
      #엔트리 세팅  
    tx=[] 
    for i in range(4):
         tx.append(Entry(win, text = ''))
         tx[i].grid(row = i*2 +1, column = 0, columnspan = 2,  padx = 40, sticky = 'new')
    
    tsearch = Entry(win, text = '')
    tsearch.place(x=380, y=200)
      #스크롤& 리스트
    scrollbar1 = Scrollbar(win, orient = VERTICAL)
    lst = Listbox(win, exportselection = 0, yscrollcommand = scrollbar1.set)
    lst.bind('<<ListboxSelect>>', on_select)
    scrollbar1.config(command = lst.yview)
    scrollbar1.grid(row = 1, column = 5, rowspan = 7, sticky = 'nes')
    lst.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, sticky = 'nsew')
      #버튼  
    titles=('add', 'update', 'delete',' Search', 'Close')
    btn=[]
    for i in range(5):
        btn.append(Button(win,  width = 12, height = 2, text = titles[i], command= lambda ii=i :on_click(ii)))
        btn[i].grid(row = 8, column = i, padx = (20,0), pady = (45,10), sticky = 'w')
def on_click(idx):
   if idx==0:on_add()      
   elif idx==1: on_update()
   elif idx==2: on_delete()
   elif idx==3:on_search()
   elif idx==4:on_close()
if __name__ == "__main__":
    win = Tk()
    preparation()
    win.mainloop()
