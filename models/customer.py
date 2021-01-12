class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, email, password, name, id):
        self.email = email
        self.password = password
        self.name = name
        self.id = id