from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Acessing the app through the main rout
@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/')
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
 
if __name__ == '__main__':
   app.run(debug = True)