class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, name, locationId, employeeId, id):
        self.name = name
        self.locationId = locationId
        self.employeeId = employeeId
        self.id = id