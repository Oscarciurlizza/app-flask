from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail

from .models.ModelPurchase import ModelPurchase
from .models.ModelBook import ModelBook
from .models.ModelUser import ModelUser

from .models.entities.User import User
from .models.entities.Book import Book
from .models.entities.Purchase import Purchase

from .consts import *
from .emails import confirm_purchase

app = Flask(__name__)


csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)
mail = Mail()


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_user_id(db, id)


@app.route("/")
@login_required
def home():
    if current_user.is_authenticated:
        if current_user.typeuser.id == 1:
            try:
                books_sold = ModelBook.list_books_sold(db)
                data = {
                    "title": "Books Sold",
                    "books_sold": books_sold
                }
                return render_template("home.html", data=data)
            except Exception as ex:
                return render_template("errors/error.html", message=format(ex))
        else:
            try:
                purchases = ModelPurchase.list_purchases_user(db, current_user)
                data = {
                    "title": "My Purchase",
                    "purchases": purchases
                }
                return render_template("home.html", data=data)
            except Exception as ex:
                return render_template("errors/error.html", message=format(ex))
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
@login_required
def buyBook():
    data_request = request.get_json()
    data = {}
    try:
        # book = Book(data_request["isbn"], None, None, None, None)
        book = ModelBook.read_book(db, data_request["isbn"])
        purchase = Purchase(None, book, current_user)
        data["success"] = ModelPurchase.register_purchase(db, purchase)
        # confirm_purchase(mail, current_user, book)
        confirm_purchase(app, mail, current_user, book)
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
    mail.init_app(app)
    app.register_error_handler(404, page_404)
    app.register_error_handler(401, page_unauthorized)
    return app
