from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/teacherlogin')
def teacherlogin():
   return render_template('teacherlogin.html')

@app.route('/studentlogin')
def studentlogin():
   return render_template('studentlogin.html')

@app.route('/teacherpage')
def teacherpage():
   return render_template('teacherpage.html')

@app.route('/insert')
def insert():
   return render_template('insert.html')

if __name__ == '__main__':
   app.run(debug = True)