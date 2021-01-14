import sqlite3
import json
from models import Employee, Location

EMPLOYEES = [
    {
        "name": "Mads Mikkelsen",
        "locationId": 2,
        "employeeId": 3,
        "id": 1
    },
    {
        "name": "Hideo Kojima",
        "locationId": 1,
        "employeeId": 1,
        "id": 2
    },
    {
        "name": "Kiefer Sutherland",
        "locationId": 2,
        "employeeId": 2,
        "id": 3
    },
    {
        "name": "Guillermo del Toro",
        "locationId": 1,
        "employeeId": 2,
        "id": 4
    },
    {
        "name": "Sweeney Todd",
        "locationId": 1,
        "employeeId": 2,
        "id": 5
    }
]


def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.address,
                e.location_id,
                l.name location_name,
                l.address location_address
            FROM Employee e
            JOIN Location l
                ON l.id = e.location_id
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # employee class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])

            # Create a Location instance from the current row
            location = Location(row['location_id'], row['location_name'], 
                                row['location_address'])

            # Add the dictionary representation of the location to the animal
            employee.location = location.__dict__

            # Add the dictionary representation of the employee to the list
            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)

# Function with a single parameter


# Function with a single parameter
def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,   
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

        return json.dumps(employee.__dict__)

def get_employees_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,   
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)

def save_employee(new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id)
        VALUES
            ( ?, ?, ?);
        """, (new_employee['name'], new_employee['address'],
                new_employee['location_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_employee['id'] = id


    return json.dumps(new_employee)
    
def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the employeeS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break        