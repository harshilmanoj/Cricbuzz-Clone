from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '101827@Hms'
app.config['MYSQL_DB'] = 'cricbuzz'

mysql = MySQL(app)

# @app.route('/test')
# def test():
#     curr  =  mysql.connection.cursor()
#     curr.execute("SELECT * FROM admin")
#     myresult = curr.fetchall()

#     # for x in myresult:
#     #     print(x)

#     return str(len(myresult))


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/createuser', methods = ['POST'])
def createuser():
    user = request.form.get('username')
    email = request.form.get('email')
    passw = request.form.get('password')

    curr  =  mysql.connection.cursor()
    curr.execute('SELECT * FROM admin;')
    myresult = curr.fetchall()
    if(len(myresult)==1):
        return myresult[0]
    else:
        st = "INSERT INTO admin (userid, email,pass) VALUES (%s, %s,%s)"
        val = (user,email,passw)
        curr.execute(st,val)
        return myresult[0]
        # return "Registerd Successfully"


@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
