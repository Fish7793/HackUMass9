from flask import Flask, render_template

app = Flask(__name__ )

@app.route("/login/")
def login():
    return ""

@app.route("/<name>")
def home(name):
    return render_template("index.html", username = name)



if __name__ == "__main__":
    app.run(debug=True)

# print("hello world")