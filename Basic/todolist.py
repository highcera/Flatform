import pymysql

class Todo:
    def __init__(self, todo,no=None, createDate=None,endDate=None):
        self.no = no
        self.todo = todo
        self.createDate = createDate
        self.endDate = endDate

    def showTodoInfo(self):
        print('번호:' , self.no)
        print('할일:' , self.todo)
        print('할일등록일:' , self.createDate)
        print('할일완료일:' , self.endDate)
        print()
        
        
class TodoDAO:
    def __init__(self):
        self.conn = None
    def connect(self):
        self.conn = pymysql.connect(host='localhost',port=3306,user='aiuser',password='aipw',db='aidb')
    def disconnect(self):
        self.conn.close()
    def insertTodo(self, todo):
        #DB접속부터시작해서 저장할 수 있는 로직을 구현 
        self.connect()  #접속 
        cur = self.conn.cursor()  #쿼리작성 
        sql = 'insert into todos(todo) values(%s)'
        cur.execute(sql,todo) #쿼리실행 
        self.conn.commit()  #커밋!!  
        self.disconnect() #접속종료 
    def updateTodo(self,no):
        #DB접속부터시작해서 저장할 수 있는 로직을 구현 
        self.connect()
        cur = self.conn.cursor()
        sql = 'update todos set end_date = current_timestamp() where no = %s'
        cur.execute(sql,no)
        self.conn.commit()
        self.disconnect()
        
    def deleteTodo(self,no):
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from todos where no = %s'
        cur.execute(sql,no)
        self.conn.commit()
        self.disconnect()
    def selectTodos(self):
        #DB접속부터시작해서 저장할 수 있는 로직을 구현 
        #2.쿼리작성
        self.connect()
        sql = 'select * from todos'
        #3.쿼리실행
        cur = self.conn.cursor()
        cur.execute(sql)
        #4.결과얻어오기
        rows = cur.fetchall()
        #5.접속종료.
        cur.close()
        self.disconnect()
        todos = []
        for row in rows:
            todo = Todo(row[1],row[0],row[2],row[3])
            todos.append(todo)
        return todos
    def selectTodosWithTodo(self,todo):
        #DB접속부터시작해서 저장할 수 있는 로직을 구현 
        #2.쿼리작성
        self.connect()
        todo = f'%{todo}%'
        sql = 'select * from todos where todo like  %s'
        #3.쿼리실행
        cur = self.conn.cursor()
        cur.execute(sql,todo)
        #4.결과얻어오기
        rows = cur.fetchall()
        #5.접속종료.
        cur.close()
        self.disconnect()
        todos = []
        for row in rows:
            todo = Todo(row[1],row[0],row[2],row[3])
            todos.append(todo)
        return todos
    def selectTodo(self,no):
        #DB접속부터시작해서 저장할 수 있는 로직을 구현 
        #2.쿼리작성
        self.connect()
        sql = 'select * from todos where no = %s'
        #3.쿼리실행
        cur = self.conn.cursor()
        cur.execute(sql,no)
        #4.결과얻어오기
        row = cur.fetchone()
        #5.접속종료.
        cur.close()
        self.disconnect()
        
        if row : 
            todo = Todo(row[1],row[0],row[2],row[3])
            return todo

class TodoManager:
    def __init__(self):
        self.dao = TodoDAO()
    def addTodo(self):
        todo = input('할일을 입력하세요. ')
        #DB에 저장할 수 있는 메소드를 호출!!  
        self.dao.insertTodo(todo)
    def endTodo(self):        
        no = input('완료한 todo의 번호를 입력해 주세요. ')
        #DB에 저장할 수 있는 메소드를 호출!!
        todo = self.dao.selectTodo(no)
        todo.showTodoInfo()
        if todo == None:
            print('존재하지 않는 번호 입니다. ')
        else : 
            self.dao.updateTodo(no)
    def findTodo(self):
        no = input('할일 번호를 입력하세요.')
        todo = self.dao.selectTodo(no)
        todo.showTodoInfo()
    def getTodos(self):
        todos = self.dao.selectTodos()
        for todo in todos: 
            todo.showTodoInfo()
    def deleteTodo(self):
        no = input('삭제할 todo의 번호를 입력해 주세요. ')
        #DB에 저장할 수 있는 메소드를 호출!!
        todo = self.dao.selectTodo(no)
        todo.showTodoInfo()
        if todo == None:
            print('존재하지 않는 번호 입니다. ')
        else : 
            self.dao.deleteTodo(no)
    
class Menu:
    def __init__(self):
        self.mgr = TodoManager()
    
    def run(self):
        while True:
            menu = int(input('1. 할일등록 2. 할일검색 3. 완료로바꾸기 4. 삭제 5. 전체출력 6. 종료 \n'))
            if menu == 1:
                #할일을 등록하기위해 필요한 코드작성.
                self.mgr.addTodo()
            elif menu == 2:
                self.mgr.findTodo()
            elif menu == 3:
                self.mgr.endTodo()
            elif menu == 4:
                self.mgr.deleteTodo()
            elif menu == 5:
                self.mgr.getTodos()
            elif menu == 6:
                break

c = TodoDAO()
#TodoDAO의 insertTodo 메서드가 잘 동작하는지 테스트!!! 
# c.insertTodo('todoList 만들기!!')
#TodoDAO의 updateTodo 메서드가 잘 동작하는지 테스트!!! 
# c.updateTodo(4);
# todos = c.selectTodos()
# for todo in todos: 
#     todo.showTodoInfo()
# todo = c.selectTodo(6)
# todo.showTodoInfo()

todos = c.selectTodosWithTodo('공부하기')
for todo in todos:
    todo.showTodoInfo()