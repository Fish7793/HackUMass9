from flask import Flask, render_template

app = Flask(__name__ )

@app.route("/login/")
def login():
    return ""

@app.route("/<name>/")
def home(name):
    return render_template("index.html", username = name, interests = "one, two, three,...", bio = "hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test")

@app.route("/find_matches/")
def matches():
    return render_template("feed.html")

@app.route("/find_friends/")
def friends():
    return render_template("friends.html")

@app.route("/chat/")
def chat():
    return render_template("chat.html")

@app.route("/settings/")
def settings():
    return render_template("userSettings.html")

# @app.route("/profile:<name>/")
# def chat():
#     return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)

# print("hello world")