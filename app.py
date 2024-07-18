from flask import Flask, make_response, redirect, url_for, render_template, request     
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return render_template('index.html')
 
@app.route('/hello/<name>') 
def hello_name(name): 
    return 'Hello %s!' % name 

@app.route('/blog/<int:postID>') 
def show_blog(postID): 
    return 'Blog Number %d' % postID 

@app.route('/rev/<float:revNo>') 
def revision(revNo): 
    return 'Revision Number %f' % revNo 

@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


# SETTING COOKIES
@app.route('/setcookie', methods = ['POST', 'GET']) 
def setcookie(): 
    if request.method == 'POST': 
        user = request.form['nm'] 
        resp = make_response(render_template('cookie.html')) 
        resp.set_cookie('userID', user) 
        return resp 

@app.route('/getcookie') 
def getcookie(): 
    name = request.cookies.get('userID') 
    return '<h1>welcome '+name+'</h1>'


if __name__=='__main__': 
   app.run(debug=True) 

