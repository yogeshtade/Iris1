from flask import Flask,render_template,request,jsonify

myapp = Flask(__name__)

@myapp.route('/')
def index():
    return render_template('index1.html')

# @myapp.route('/get_data',methods = ['POST'])
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']

#     print(data,data1)

#     return 'Data Received'


# @myapp.route('/get_data',methods = ['GET','POST'])
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']

#     print(data,data1)

#     return 'Data Received'


# @myapp.route('/get_data',methods = ['GET','POST'])
# def get_data():
#     if request.method == 'POST':
#         data = request.form['var']
#         data1 = request.form['var1']

#         print(data,data1)
#     else:
#         print('Data not received')

#     return 'Data Received'

# @myapp.route('/get_data') # Default GET method
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']

#     print(f'{data=},{data1=}')

#     return 'Data Received'


# @myapp.route('/get_data',methods=['GET','POST']) # Default GET method
# def get_data():
#     data = request.form['var']
#     data1 = request.form['var1']

    # print(f'{data=},{data1=}')

#     return 'Data Received'


# @myapp.route('/get_data',methods = ['GET','POST'])
# def get_data():
#     data = request.form

#     print(f"{data=}")
#     print(type(data))

#     return 'Data Received'

# @myapp.route('/get_data',methods = ['GET','POST'])
# def get_data():
#     data = request.form

#     print(f"{data=}")
#     print(type(data))
#     data_from_imm = data['var1']
#     print(data_from_imm)

#     return render_template('index1.html')

# @myapp.route('/get_data',methods = ['GET','POST'])
# def get_data():
#     data = request.form

#     print(f"{data=}")
#     print(type(data))
#     data_from_imm = data['var1']
#     print(data_from_imm)

#     return jsonify(data)

# @myapp.route('/get_data',methods = ['GET','POST'])
# def get_data():
#     data = request.get_json() # Data is in form of dict

#     print(f"{data=}")
#     print(type(data))
#     data_from_imm = data['var1']
#     print(data_from_imm)

#     return jsonify(data)


@myapp.route('/getdata',methods = ['GET','POST'])
def get_data():
    data = request.json # Data is in form of dict

    print(f"{data=}")
    print(type(data))
    data_from_imm = data['var1']
    print(data_from_imm)

    return jsonify(data)

@myapp.route('/data',methods=['GET','POST'])
def data():
    var = request.args ## This for query params
    print(var)
    print(type(var))

    return jsonify(var)

if __name__ == '__main__':
    myapp.run(debug = True)