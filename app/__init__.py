from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from .models.ModelBook import ModelBook
from .models.ModelUser import ModelUser

from .models.entities.User import User
from .models.entities.Book import Book

from .consts import *

app = Flask(__name__)


csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_user_id(db, id)


@app.route("/")
@login_required
def home():
    if current_user.is_authenticated:
        if current_user.typeuser.id == 1:
            books_sold = []
            data = {
                "title": "Books Sold",
                "books_sold": books_sold
            }
        else:
            my_purchase = []
            data = {
                "title": "My Purchase",
                "purchase": my_purchase
            }
        return render_template("home.html", data=data)
    else:
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User(None, request.form["username"],
                    request.form["password"], None)
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            login_user(logged_user)
            flash(SUCCESSFUL_LOGIN)
            return redirect(url_for("home"))
        else:
            flash(ERROR_LOGIN, "danger")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash(SUCCESSFUL_LOGOUT, "success")
    return redirect(url_for("login"))


@app.route("/books")
@login_required
def list_books():
    try:
        books = ModelBook.list_books(db)
        data = {
            "title": "Books",
            "books": books
        }
        return render_template("list_books.html", data=data)
    except Exception as ex:
        return render_template("errors/error.html", message=format(ex))


@app.route("/buyBook", methods=["POST"])
def buyBook():
    data_request = request.get_json()
    print(data_request)
    data = {}
    try:
        book = Book()
        data["success"] = True
    except Exception as ex:
        data["message"] = format(ex)
        data["success"] = False
    return jsonify()


def page_404(error):
    return render_template("errors/404.html"), 404


def page_unauthorized(error):
    return redirect(url_for("login"))

# Patron singleton - nos permite tener una sola instancia de nuestra aplicacion y trabajar con ella en todo el proyecto


def init_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, page_404)
    app.register_error_handler(401, page_unauthorized)
    return app
