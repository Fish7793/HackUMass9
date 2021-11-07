from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__ )
user = ""

@app.route("/login.html/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
    #     # passw = request.form["password"]
        return redirect(url_for("home", usr = user))
    else:
        return render_template("login.html")

@app.route("/templates/templates/login.html/")
def templatesLogin():
    return redirect(url_for("login"))



@app.route("/templates/signup.html/")
def signup():
    return render_template("signup.html")

@app.route("/templates/templates/signup.html/")
def templatesSignup():
    return redirect(url_for("signup"))


@app.route("/templates/index.html/<usr>")
def home(usr):
    return render_template("index.html", username = usr)
    # , interests = "one, two, three,...", bio = "hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test"

@app.route("/templates/templates/index.html/")
def templatesHome():
    return redirect(url_for("home", usr = user))

@app.route("/templates/index.html/")
def templatesHome2():
    return render_template("index.html", username = user)




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