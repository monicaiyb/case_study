from flask import Flask, redirect, url_for, request, render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

# Creating the database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'case'

mysql = MySQL(app)

# Acessing the app through the main rout
@app.route('/')
def about():
    return render_template('form.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        details = request.form
        name = details['name']
        phone=details['phone']
        email = details['email']
        password = details['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO farmers(name, phone, email,password) VALUES (%s,%s, %s,%s)", (name, phone, email, password))
        mysql.connection.commit()
        msg = 'You have successfully registered!'
        cur.close()
        return 'success'
    return render_template('form.html')
 
if __name__ == '__main__':
   app.run(debug = True)