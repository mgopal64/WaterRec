from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
    return render_template("data.html")

@app.route("/data")
def data():
    return render_template("data.html")

if __name__ == "__main__":
    app.run()