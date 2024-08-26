# # importing redirect 
# from flask import Flask, redirect, url_for, render_template, request 

# # Initialize the flask application 
# app = Flask(__name__) 

# # It will load the form template which 
# # is in login.html 
# @app.route('/') 
# def index(): 
# 	return render_template("login.html") 


# @app.route('/success') 
# def success(): 
# 	return "logged in successfully"

# # loggnig to the form with method POST or GET 
# @app.route("/login", methods=["POST", "GET"]) 
# def login(): 
	
# 	# if the method is POST and Username is admin then 
# 	# it will redirects to success() url. 
# 	if request.method == "POST" and request.form["username"] == "admin": 
# 		return redirect(url_for("success"), code=302) 

# 	# if the method is GET or username is not admin, 
# 	# then it redirects to index method. 
# 	return redirect(url_for('index')) 


# if __name__ == '__main__': 
# 	app.run(debug=True) 


# importing abort 
from flask import Flask, abort 

# Initialize the flask application 
app = Flask(__name__) 


@app.route('/<String:uname>') 
def index(uname): 
	if uname[0].isdigit(): 
		abort(400) 
	return '<h1>Good Username</h1>'


if __name__ == '__main__': 
	app.run()
