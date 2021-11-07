from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = "1234"

@app.route("/login.html/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        session["user"] = user
        # passw = request.form["password"]
        # session["pass"] = passw
        return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/templates/templates/login.html/")
def templatesLogin():
    return redirect(url_for("login"))



@app.route("/templates/interests.html", methods = ["POST", "GET"])
def interests():
    if request.method == "POST":
        bio = request.form["biography"]
        session["bio"] = bio
        # user = request.form["username"]
        # session["user"] = user
        # passw = request.form["password"]
        # session["pass"] = passw
        return redirect(url_for("home"))
    else:
        return render_template("interests.html")


@app.route("/templates/signup.html/", methods = ["POST", "GET"])
def signup():
    if request.method == "POST":
        user = request.form["username"]
        session["user"] = user
        # passw = request.form["password"]
        # session["pass"] = passw
        return redirect(url_for("interests"))
    else:
        return render_template("signup.html")

@app.route("/templates/templates/signup.html/")
def templatesSignup():
    return redirect(url_for("signup"))






@app.route("/templates/index.html/")
def home():
    if "user" in session:
        username = session["user"]
        return render_template("index.html")
    else:
        return redirect(url_for("login"))
    # , interests = "one, two, three,...", bio = "hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test hello, this is a test"

@app.route("/templates/templates/index.html/")
def templatesHome():
    return redirect(url_for("home"))





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





@app.route("/templates/userSettings.html/")
def settings():
    return render_template("userSettings.html")

@app.route("/templates/templates/userSettings.html/")
def templatesUserSettings():
    return redirect(url_for("settings"))






if __name__ == "__main__":
    app.run(debug=True)
