from threading import Thread
from flask_mail import Message
from flask import current_app, render_template


""" def confirm_purchase(mail, user, book):
    try:
        message = Message("Book purchase confirmation",
                          sender=current_app.config["MAIL_USERNAME"],
                          recipients=["bciurlizzaoscar@crece.uss.edu.pe"])
        message.html = render_template(
            "emails/confirm_purchase.html", user=user, book=book)
        mail.send(message)
    except Exception as ex:
        raise Exception(ex) """


def confirm_purchase(app, mail, user, book):
    try:
        message = Message("Book purchase confirmation",
                          sender=current_app.config["MAIL_USERNAME"],
                          recipients=["bciurlizzaoscar@crece.uss.edu.pe"])
        message.html = render_template(
            "emails/confirm_purchase.html", user=user, book=book)
        thread = Thread(target=send_email_async, args=[app, mail, message])
        thread.start()
    except Exception as ex:
        raise Exception(ex)


def send_email_async(app, mail, message):
    with app.app_context():
        mail.send(message)
