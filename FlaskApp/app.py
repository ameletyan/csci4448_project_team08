# As of now, this page imports Flask and uses whatever is in index.html as the home page

from flask import Flask, render_template	# Imports all necessary functions
app = Flask(__name__)						# Initializes app

@app.route("/")								# Sets homepage
def main():
	return render_template('index.html')	# Renders index.html in /templates/index.html

if __name__ == "__main__":
	app.run()								# Runs app
