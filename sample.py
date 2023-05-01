from flask import Flask
import sum

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("hoge")
    result = sum.sum(1, 2)
    return f"<p>Hello, World! {result}</p>"
