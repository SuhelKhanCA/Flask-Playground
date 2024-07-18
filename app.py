from flask import Flask, flash, make_response, redirect, url_for, render_template, request     
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)   # Flask constructor 
app.secret_key = os.urandom(24)
app.config['SECRET_KEY'] = os.urandom(24)  
# A decorator used to tell the application 
# which URL is associated function 
# @app.route('/')       
# def hello(): 
#     return render_template('index.html')
 
# @app.route('/hello/<name>') 
# def hello_name(name): 
#     return 'Hello %s!' % name 

# @app.route('/blog/<int:postID>') 
# def show_blog(postID): 
#     return 'Blog Number %d' % postID 

# @app.route('/rev/<float:revNo>') 
# def revision(revNo): 
#     return 'Revision Number %f' % revNo 

@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello Admin'


# @app.route('/guest/<guest>')
# def hello_guest(guest):  # binding to hello_guest call
#     return 'Hello %s as Guest' % guest


# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':  # dynamic binding of URL to function
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))


# # SETTING COOKIES
# @app.route('/setcookie', methods = ['POST', 'GET']) 
# def setcookie(): 
#     if request.method == 'POST': 
#         user = request.form['nm'] 
#         resp = make_response(render_template('cookie.html')) 
#         resp.set_cookie('userID', user) 
#         return resp 

# @app.route('/getcookie') 
# def getcookie(): 
#     name = request.cookies.get('userID') 
#     return '<h1>welcome '+name+'</h1>'

# #FILE UPLOADING IN FLASK
# @app.route('/upload')
# def upload_file1():
#     return render_template('upload.html')

# @app.route('/uploader', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#       f = request.files['file'] 
#       f.save(secure_filename(f.filename)) 
#       return 'file uploaded successfully'


# Sending From Data to the HTML file of the server

@app.route('/')
def student():
    return render_template('student.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)
    
@app.route('/login', methods=['GET', 'POST'])
# login function verify username and password
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again !'
        else:

            # flashes on successful login
            flash('You were successfully logged in')
            return redirect(url_for('hello_admin'))
    return render_template('login.html', error=error)    
if __name__=='__main__': 
   app.run(debug=True) 

