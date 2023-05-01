from flask import Flask
import sum

app = Flask(__name__)


@app.route("/")
def hello_world():
    result = sum.sum(1, 2)
    print(f"### result is {result} ###")
    return f"<p>Hello, World! {result}</p>"


# app.run()があることで、普通のpythonコードとして起動可能
# デバッガと組み合わせるときは、こちらの起動方法がやりやすそう
if __name__ == "__main__":
    app.run()
