from flask import Flask, render_template

app = Flask(__name__ )

@app.route("/login/")
def login():
    return ""

@app.route("/<name>/")
def home(name):
    return render_template("index.html", username = name, interests = "one, two, three,...", bio = "hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test")



if __name__ == "__main__":
    app.run(debug=True)

# print("hello world")