from flask import Flask
app = Flask(name)

@app.route('/')
def main():
    return '<h1>Main page</h1>'

@app.route('/contact')
def contact():
    return '<h1>contact</h1>'