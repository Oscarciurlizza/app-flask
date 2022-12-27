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


1
