EMPLOYEES = [
    {
        "name": "Mads Mikkelsen",
        "locationId": 2,
        "animalId": 3,
        "id": 1
    },
    {
        "name": "Hideo Kojima",
        "locationId": 1,
        "animalId": 1,
        "id": 2
    },
    {
        "name": "Kiefer Sutherland",
        "locationId": 2,
        "animalId": 2,
        "id": 3
    },
    {
        "name": "Guillermo del Toro",
        "locationId": 1,
        "animalId": 2,
        "id": 4
    },
    {
        "name": "Sweeney Todd",
        "locationId": 1,
        "animalId": 2,
        "id": 5
    }
]


def get_all_employees():
    return EMPLOYEES

# Function with a single parameter


def get_single_employee(id):
    # Variable to hold the fouemployee, if it exists
    requested_employee = None

    # Iterate temployeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
