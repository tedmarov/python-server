CUSTOMERS = [
    {
        "email": "matt@berry.com",
        "password": "notreal",
        "name": "Matt Berry",
        "id": 1
    },
    {
        "email": "taika@waititi.com",
        "password": "fakethree",
        "name": "Taika Waititi",
        "id": 2
    },
    {
        "email": "jemaine@clement.com",
        "password": "faketoo",
        "name": "Jemaine Clement",
        "id": 3
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the customerS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
