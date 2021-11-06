from flask import Flask, render_template, redirect, url_for

app = Flask(__name__ )

@app.route("/")
def login():
    return render_template("login.html")




@app.route("/<name>/")
def home(name):
    return render_template("index.html", username = name, interests = "one, two, three,...", bio = "hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test")





@app.route("/templates/feed.html/")
def matches():
    return render_template("feed.html")

@app.route("/templates/templates/feed.html/")
def templatesMatches():
    return redirect(url_for("matches"))





@app.route("/templates/friends.html/")
def friends():
    return render_template("friends.html")

@app.route("/templates/templates/friends.html/")
def templatesFriends():
    return redirect(url_for("friends"))

# @app.route("/chat/")
# def chat():
#     return render_template("chat.html")




@app.route("/templates/userSettings.html/")
def settings():
    return render_template("userSettings.html")

@app.route("/templates/templates/userSettings.html/")
def templatesUserSettings():
    return redirect(url_for("settings"))

# @app.route("/profile:<name>/")
# def chat():
#     return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)

# print("hello world")