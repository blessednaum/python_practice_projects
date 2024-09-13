from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/<name>')
def myname(name):
    return "Heloo I am , {}".format(name)

if __name__ == "__main__":
    app.run(debug=True)