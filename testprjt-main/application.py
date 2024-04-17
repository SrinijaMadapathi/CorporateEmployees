import boto3 
import json
import mysql.connector
from flask import Flask,render_template,request
from config import *

app = Flask(__name__)

client = boto3.client('secretsmanager', region_name='us-east-1')

response = client.get_secret_value(
  SecretId='Teststr1'
   )
database_secrets = json.loads(response['SecretString'])
username = database_secrets['username']
    
response = client.get_secret_value(
    SecretId='Teststr1'
    )
database_secrets = json.loads(response['SecretString'])
password = database_secrets['password']

db_conn = mysql.connector.connect(
    host=hostname,
    port=3306,
    user=username,
    password=password,
    database=Database)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')


@app.route("/addemployee", methods=['GET','POST'])
def AddEmployee():
    return render_template('AddEmp.html')

  
@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    pri_skill = request.form['pri_skill']
    Department = request.form['Department']

    add_data = "INSERT INTO Emp ( emp_id ,first_name, last_name, pri_skill, Department) VALUES (%s, %s, %s, %s, %s)"

    data = (emp_id, first_name, last_name, pri_skill, Department)
    cursor = db_conn.cursor()

    cursor.execute(add_data, data)
    db_conn.commit()
    emp_name = "" + first_name + " " + last_name
        
    cursor.close()

    print("all modification done...")
    return render_template('AddEmpOutput.html', name=emp_name)

@app.route("/getemployee", methods=['GET','POST'])
def GetEmployee():
    return render_template('GetEmp.html')

@app.route("/fetchdata", methods=['POST'])
def GetEmp():
    cursor = db_conn.cursor()
    emp_id = request.form['emp_id']
    query = "SELECT * FROM Emp WHERE emp_id = %s"

    try:
        cursor.execute(query, (emp_id,))
        myresult = cursor.fetchall()
        print(myresult)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
    return render_template('GetEmpOutput.html',name = myresult)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
