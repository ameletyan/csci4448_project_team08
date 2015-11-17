# Import flask module and create an app using Flask
from flask import Flask, render_template, json, request				# Need to run "pip install flask"
from flask.ext.mysql import MySQL									# Need to run "pip install flask-mysql"
from werkzeug import generate_password_hash, check_password_hash	# Need "werkzeug"

app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
# Some overhead stuff was down outside of the code to make the database work with the following code
app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# Add basic route "/" and its corresponding request handler
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

def signUp():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
 
    # validate the received values
    if _name and _email and _password:
		conn = mysql.connect()									# This is where we use "flask.ext.mysql"
		cursor = conn.cursor()
		_hashed_password = generate_password_hash(_password)	# This is where we use "werkzeug"
		cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
		data = cursor.fetchall()
		
		if len(data) is 0:
			conn.commit()
			return json.dumps({'message':'User created successfully !'})
		else:
			return json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

# Run the app
if __name__ == "__main__":
	app.run()
