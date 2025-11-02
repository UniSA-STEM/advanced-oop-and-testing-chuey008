'''
File: staff.py
Description: This class Staff file plays a role in the zoo operations from zookeepers to vets. Some actions include
feeding animals, cleaning enclosures, and health checks.
Author: Emily Chuong
ID: 110448094
Username: chuey008
This is my own work as defined by the University's Academic Integrity Policy.
'''

# will need to import from animal

class Staff:
    def __init__(self, staff_id, name, role):
        """
        This class represents a staff member who has tasks depending on their role.
        Private attributes will continue to be used for encapsulation and ensuring no changes are made.
        Adding validation checks to make sure what is entered is true.
        Checks to see if staff_id and name is a string and not empty.
        Role must only be either vet or zookeeper.
        """
        self.__validate_init(staff_id, name, role)
        self.__staff_id = staff_id
        self.__role = role

    def __validate_init(self, staff_id, name, role):
        """
        Internal validator to help conduct checks for testing.
        """
        if not isinstance(staff_id, str) or not staff_id.strip():
            raise ValueError("Staff ID cannot be an empty string.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be an empty string.")
        if role not in ("Veterinarian", "Zookeeper"):
            raise ValueError("Role must be either 'Veterinarian' or 'Zookeeper'.")

    # using @property decorator to transform a method into a getter
    def staff_id(self):
        # public staff identifier
        return self.__staff_id

    def name(self):
        # public name identifier
        return self.__name

    def role(self):
        # public role identifier
        return self.__role

