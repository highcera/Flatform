from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

# CSV 파일의 경로
csv_path = 'P:/data.csv'

# CSV 파일에서 데이터를 읽는 함수
def read_data():
    with open(csv_path, newline='', encoding='cp949') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

# CSV 파일에 데이터를 쓰는 함수
def write_data(data):
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'gender', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# 메인 페이지를 표시하는 라우트
@app.route('/')
def index():
    data = read_data()
    return render_template('index.html', data=data)

# 데이터를 추가하는 라우트
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    data = read_data()
    data.append({'name': name, 'gender': gender, 'age': age})
    write_data(data)
    return redirect('/')

# 데이터를 수정하는 라우트
@app.route('/update', methods=['POST'])
def update():
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    data = read_data()
    for i, row in enumerate(data):
        if row['name'] == name:
            data[i] = {'name': name, 'gender': gender, 'age': age}
            write_data(data)
            return redirect('/')
    return 'Not Found'

# 데이터를 삭제하는 라우트
@app.route('/delete', methods=['POST'])
def delete():
    name = request.form['name']
    confirm = request.form.get('confirm')
    if confirm == 'true':
        data = read_data()
        for i, row in enumerate(data):
            if row['name'] == name:
                del data[i]
                write_data(data)
                return redirect('/')
        return 'Not Found'
    else:
        return 'Confirm'



# # 데이터를 삭제하는 라우트
# @app.route('/delete', methods=['POST'])
# def delete():
#     name = request.form['name']
#     data = read_data()
#     for i, row in enumerate(data):
#         if row['name'] == name:
#             return render_template('delete.html', name=name)
#     return 'Not Found'

# # 데이터를 실제로 삭제하는 라우트
# @app.route('/delete_confirm', methods=['POST'])
# def delete_confirm():
#     name = request.form['name']
#     data = read_data()
#     for i, row in enumerate(data):
#         if row['name'] == name:
#             del data[i]
#             write_data(data)
#             return 'Success'
#     return 'Not Found'

if __name__ == '__main__':
    app.run()