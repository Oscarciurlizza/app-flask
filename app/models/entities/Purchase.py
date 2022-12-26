class Purchase():
    def __init__(self, uuii, user, book, date=None):
        self.uuii = uuii
        self.book = book
        self.user = user
        self.date = date
