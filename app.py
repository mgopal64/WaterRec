from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return "<p>About</p>"
