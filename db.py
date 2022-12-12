from flask import Flask,render_template,request,jsonify
import mysql.connector


myapp = Flask(__name__)

@myapp.route('/')
def index():
    return render_template('index1.html')

@myapp.route('/student_data',methods=["POST"])
def student_data():
    s_name = request.form['student_name']
    s_rollno = request.form['student_roll_no']
    s_sub1 = request.form['student_sub1']
    s_sub2 = request.form['student_sub2']
    s_sub3 = request.form['student_sub3']

    print(f"student Name = {s_name}")


    conn = mysql.connector.connect(host='localhost',
                                    database='may',
                                    user='root',
                                    password='Yogesh@1996')

    cursor = conn.cursor()
    query = "INSERT INTO student_s (name,roll_no,subject1,subject2,subject3) VALUES (%s,%s,%s,%s,%s)"
    data = (s_name,s_rollno,s_sub1,s_sub2,s_sub3)

    cursor.execute(query,data)

    conn.commit()
    conn.close()

    return jsonify(data)

if __name__ == '__main__':
    myapp.run(debug = True)