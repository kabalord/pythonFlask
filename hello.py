from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/contact')
def contact():
    return '<h1>contact</h1>'