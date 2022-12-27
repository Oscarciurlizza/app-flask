class Purchase():
    def __init__(self, uuid, book, user, date=None):
        self.uuid = uuid
        self.book = book
        self.user = user
        self.date = date
