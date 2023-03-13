from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# setup
app = Flask(__name__, static_url_path='/static', template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # SQLite
        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        # HTML form
        name = request.form['username']
        password = request.form['password']
        email = request.form['email']
        print(name, password, email)

        # query/comparing the name of the form to the name of the database
        query = "SELECT name, password FROM users WHERE name='"+name+"' AND password='"+password+"' AND email='"+email+"'"
        cursor.execute(query)

        results = cursor.fetchall()

        # validation
        if len(results) == 0:
            print("try again")
        else:
            return redirect(url_for('upload_file'))

    return render_template('login.html')


    
@app.route('/error_login')
def error_login():
    return '<h1>error login, try again</h1>'

# @app.route('/upload', methods=['GET'])
# def upload_file():
#     return render_template('upload_file.html')

