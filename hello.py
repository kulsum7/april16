# pip install Flask
# hello.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

# Define a route to hello_world function
@app.route('/')
def pdfGenerator():
	return 'Hello PDF file!'

# Run the app on http://localhost:8085
app.run(debug=True,port=9090)

#python hello.py