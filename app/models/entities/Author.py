class Author():

    def __init__(self, id, lastname, name, birth=None):
        self.id = id
        self.lastname = lastname
        self.name = name
        self.birth = birth

    def full_name(self):
        return "{0}, {1}".format(self.lastname, self.name)
