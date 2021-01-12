ANIMALS = [
    {
        "name": "Buttered Oodles",
        "breed": "Poodle",
        "customerId": 1,
        "locationId": 2,
        "id": 1
    },
    {
        "name": "Bubba",
        "breed": "Catfish",
        "customerId": 2,
        "locationId": 1,
        "id": 2
    },
    {
        "name": "Coffee",
        "breed": "Bean Dog",
        "customerId": 3,
        "locationId": 2,
        "id": 3
    },
    {
        "name": "Mr. Spoons",
        "breed": "Silverware",
        "customerId": 3,
        "locationId": 2,
        "id": 4
    }
]


def get_all_animals():
    return ANIMALS

# Function with a single parameter


def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal