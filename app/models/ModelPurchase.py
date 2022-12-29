from .entities.Purchase import Purchase
from .entities.Book import Book


class ModelPurchase():

    @classmethod
    def register_purchase(self, db, purchase):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO purchase (uuid, book_isbn, user_id)
                    VALUES (uuid(), '{0}', {1})""".format(purchase.book.isbn, purchase.user.id)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def list_purchases_user(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT PUR.date, BOK.isbn, BOK.title, BOK.price 
                    FROM purchase PUR JOIN book BOK ON PUR.book_isbn = BOK.isbn
                    WHERE PUR.user_id = {0} ORDER BY PUR.date DESC""".format(user.id)
            cursor.execute(sql)
            data = cursor.fetchall()
            purchases = []
            for row in data:
                book = Book(row[1], row[2], None, None, row[3])
                purchase = Purchase(None, book, user, row[0])
                purchases.append(purchase)
            print(purchases)
            return purchases
        except Exception as ex:
            raise Exception(ex)
