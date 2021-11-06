from flask import Flask, render_template

app = Flask(__name__ )

@app.route("/login/")
def login():
    return ""

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()

# print("hello world")