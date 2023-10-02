import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)

#inom route("") skapar man bara path så att säga, jag väljer. 
@bp.route("/") #controller. betyder att detta hanterar inkommande HTTP reqs.
def index():
    user = model.User(1, "mary@example.com", "mary")
    posts = [
        model.Message(
            1, user, "Test post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            2, user, "Another post", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(
            3, user, "Third post", datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/index.html", posts=posts) #funktionen kallar på main/index.html och skickar med posts.

@bp.route("/userprofile") #don't have to create new bp, use the same. but have to create new path. 
def user():
    user = model.User(1, "erik@example.com", "erik")
    posts = [
        model.Message(1, user, "Test post hello hello", datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/userprofile.html", user=user, posts=posts) 

@bp.route("/displaypost")
def post():
    user = model.User(1,"erik@example.com", "erik")
    posts = [
        model.Message(1, user, "Test post hello hello", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(1, user, "Test post hello hello", datetime.datetime.now(dateutil.tz.tzlocal())
        ),
        model.Message(1, user, "Test post hello hello", datetime.datetime.now(dateutil.tz.tzlocal())
        )
    ]
    return render_template("main/displaypost.html", user=user, posts=posts)