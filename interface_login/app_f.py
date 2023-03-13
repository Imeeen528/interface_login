from flask import Flask, render_template, request, redirect, url_for
#You use create_access_token() to make JSON Web Tokens, jwt_required() to protect routes, and get_jwt_identity() to get the identity of a JWT in a protected route.
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import JWTManager
import sqlite3

# setup
app = Flask(__name__, static_url_path='/static', template_folder='templates')

# Setup the Flask-JWT-Extended extension / secret to encode each web token , should be very complex and long
# app.config["JWT_SECRET_KEY"] = "uihzeeuidghzdbchgzygeuzad65d98"  
# jwt = JWTManager(app)

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
            return render_template('upload_file')

    return render_template('login.html')


    
# @app.route('/error_login')
# def error_login():
#     return '<h1>error login, try again</h1>'

@app.route('/upload', methods=['GET'])
def upload_file():
    return render_template('upload_file.html')

