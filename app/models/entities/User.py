from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, password, typeuser):
        self.id = id
        self.username = username
        self.password = password
        self.typeuser = typeuser

    @classmethod
    def verify_password(self, encrypted, password):
        return check_password_hash(encrypted, password)
