from werkzeug.security import check_password_hash
from .entities.User import User
from .entities.TypeUser import TypeUser


class ModelUser():
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password
                    FROM user WHERE username = '{0}'""".format(user.username)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                coincide = User.verify_password(data[2], user.password)
                if coincide:
                    logged_user = User(data[0], data[1], None, None)
                    return logged_user
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT USU.id, USU.username, TYP.id, TYP.name
                    FROM user USU JOIN typeuser TYP ON USU.typeuser_id = TYP.id 
                    WHERE USU.id = {0}""".format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            typeuser = TypeUser(data[2], data[3])
            logged_user = User(data[0], data[1], None, typeuser)
            return logged_user
        except Exception as ex:
            raise Exception(ex)
