from cs50 import SQL
from flask import Flask, render_template, request, session
from flask_session import Session

# creates flask web application
app = Flask(__name__)

# configures session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# links app to database
db = SQL("sqlite:///speedle.db")

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game", methods=["POST", "GET"])
def game():

    if request.method == "POST":

        stats = db.execute("SELECT averageScore, played FROM users WHERE cache = ?", session["user_id"])
        newScore = float(request.form.get("score"))

        averageScore = stats[0]["averageScore"]
        played = stats[0]["played"]
        newAverageScore = (averageScore * played + newScore) / (played + 1)
        db.execute("UPDATE users SET averageScore = ?, played = ? WHERE cache = ?", newAverageScore, played + 1, session["user_id"])

        return render_template("game.html")

    if request.method == "GET":

        if session.get("user_id") is None:
            lastUser = db.execute("SELECT cache FROM users ORDER BY cache DESC limit 5")[0]["cache"]
            session["user_id"] = lastUser + 1
            db.execute("INSERT INTO users (cache, averageScore, played) VALUES(?, 0, 0)", session["user_id"])

        averageScore = round(db.execute("SELECT averageScore FROM users WHERE cache = ?", session["user_id"])[0]["averageScore"], 3)
        return render_template("game.html", averageScore=averageScore)
