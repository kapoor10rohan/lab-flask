from flask import Flask

app = Flask(__name__)

@app.route("/")
def info():
    a="Company Name: ABC Corporation<br/>"
    b="Location: India<br/>"
    c="Contact Detail: 999-999-9999"
    return a+b+c
    
@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation"

if __name__=="__main__":
    app.run(host="0.0.0.0")