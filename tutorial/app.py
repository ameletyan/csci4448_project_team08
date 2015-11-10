# Import flask module and create an app using Flask
from flask import Flask
app = Flask(__name__)

# Add basic route "/" and its corresponding request handler
@app.route("/")
def main():
	return "Welcome!"

# Run the app
if __name__ == "__main__":
	app.run()