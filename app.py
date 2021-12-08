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
def home():
   return render_template('index.html')

@app.route('/register')
def about():
    return render_template('form.html')

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
        return render_template('farmer.html')
    return render_template('farmer.html')
# Route to display all farmers

@app.route('/farmers') 
def farmer(): 
    cur = mysql.connection.cursor()
    #execute select statement to fetch data to be displayed in combo/dropdown
    cur.execute('SELECT * FROM farmers') 
    #fetch all rows ans store as a set of tuples 
    farmerlist = cur.fetchall() 
    #render template and send the set of tuples to the HTML file for displaying
    return render_template('farmer.html',farmerlist=farmerlist)

#Routes for the milk delivery


@app.route('/make_delivery',methods = ['POST', 'GET'])
def delivery_form():
  if request.method == "POST":
        details = request.form
        farmer_name = details['farmer_name']
        address=details['address']
        location = details['location']
        quantity = details['quantity']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO deliveries(farmer_name, address, location,quantity) VALUES (%s,%s, %s,%s)", (farmer_name, address, location, quantity))
        mysql.connection.commit()
        cur.close()
        return render_template('delivery.html')
  return render_template('delivery_form.html')
  

@app.route('/delivery')
def milk_delivery():
    cur = mysql.connection.cursor()
    #execute select statement to fetch data to be displayed in combo/dropdown
    cur.execute('SELECT * FROM deliveries') 
    #fetch all rows ans store as a set of tuples 
    deliverylist = cur.fetchall() 
    return render_template('delivery.html',deliverylist=deliverylist)      
 
if __name__ == '__main__':
   app.run(debug = True)