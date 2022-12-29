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

    @classmethod
    def read_book(self, db, isbn):
        try:
            cursor = db.connect.cursor()
            sql = """SELECT isbn, title, edition, price 
                    FROM book WHERE isbn = '{0}'""".format(isbn)
            cursor.execute(sql)
            data = cursor.fetchone()
            book = Book(data[0], data[1], None, data[2], data[3])
            return book
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def list_books_sold(self, db):
        try:
            cursor = db.connect.cursor()
            sql = """SELECT PUR.book_isbn, BOK.title, BOK.price,
                    COUNT(PUR.book_isbn) AS sold_units  
                    FROM purchase PUR JOIN book BOK ON PUR.book_isbn = BOK.isbn 
                    GROUP BY PUR.book_isbn ORDER BY 4 DESC, 2 ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            books = []
            for row in data:
                book = Book(row[0], row[1], None, None, row[2])
                book.sold_units = int(row[3])
                books.append(book)
            return books
        except Exception as ex:
            raise Exception(ex)
