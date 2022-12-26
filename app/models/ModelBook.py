from .entities.Author import Author
from .entities.Book import Book


class ModelBook():
    @classmethod
    def list_books(self, db):
        try:
            cursor = db.connect.cursor()
            sql = """SELECT BOK.isbn, BOK.title, BOK.edition, BOK.price,
                AUTH.lastname, AUTH.name
                FROM book BOK JOIN author AUTH ON BOK.author_id = AUTH.id 
                ORDER BY BOK.title ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            books = []
            for row in data:
                auth = Author(0, row[4], row[5])
                book = Book(row[0], row[1], auth, row[2], row[3])
                books.append(book)
            return books
        except Exception as ex:
            raise Exception(ex)
