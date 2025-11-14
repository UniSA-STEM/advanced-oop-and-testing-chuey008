'''
File: staff.py
Description: This class Staff file plays a role in the zoo operations from zookeepers to vets. Some actions include
feeding animals, cleaning enclosures, and health checks.
Author: Emily Chuong
ID: 110448094
Username: chuey008
This is my own work as defined by the University's Academic Integrity Policy.
'''

from typing import List
from datetime import date
from animal import Animal, HealthRecord

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

    # --------------------------- Public Properties ---------------------------
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

    # --------------------------- Assignment Helpers ---------------------------
    def assign_animal(self, animal):
        """
        This will assign an animal to the staff member.
        Method stores the animal's name only, this is to avoid duplicating object references.
        Checks to see if what is chosen is an actual animal.
        """
        if not isinstance(animal, Animal):
            raise TypeError("animal must be an Animal instance.")
        if animal.name not in self.__assigned_animals:
            self.__assigned_animals.append(animal.name)

    def assign_enclosure(self, enclosure_name):
        """
        This will assign an enclosure to the staff member.
        Checks to see if what is chosen is an actual enclosure, needs to be a string and not empty.
        """
        if not isinstance(enclosure_name, str) or not enclosure_name.strip():
            raise ValueError("enclosure_name cannot be an empty string.")
        if enclosure_name not in self.__assigned_enclosures:
            self.__assigned_enclosures.append(enclosure_name.strip())

    # --------------------------- Role Specific Actions ---------------------------
    def feed_animal(self, animal: Animal, food):
        """
        Feeding the animal is done by the zookeepers.
        If the staff is not a zookeeper, then it will raise a PermissionError.
        If the animal is undergoing treatment, it will print a message to prevent feeding.
        Otherwise, it will be delegated to animl.eat(food) which will self validate
        """
        if self.__role != "Zookeeper":
            raise PermissionError("only Zookeepers are able to feed the animals.")
        if not isinstance(animal, Animal):
            raise TypeError("animal must be an Animal instance.")
        if animal.under_treatment:
            return f"{animal.name} is undergoing treatment, and should not be fed without vet approval."
        return animal.eat(food)

    def clean_enclosure(self, enclosure):
        """
        Cleaning an enclosure is done by zookeepers.
        The parameter for the enclosure is to implement a 'clean' method and 'name' property
        Returning the staff name and enclosure status.
        """
        if self.__role != "Zookeeper":
            raise PermissionError("only Zookeepers are able to clean the enclosures.")
        result = enclosure.clean()
        return f"{self.__name} cleaned enclosure '{enclosure.name}' - {result}."

    def perform_health_check(self, animal: Animal, description, severity):
        """
        Performing a health check is done by veterinarians.
        If the staff is not a vet, the nit will raise a PermissionError.
        Validate that the animal is an Animal instance.
        Description cannot be an empty string.
        Severity is between 1 and 10.
        HealthRecord to be stamped with today's date.
        Adding the record to the animal which updates its under_treatment status.
        Return the health record for the animal using vet name, animal name, and severity.
        """
        if self.__role != "veterinarian":
            raise PermissionError("only veterinarians are allowed to perform health checks on the animals.")
        if not isinstance(animal, Animal):
            raise TypeError("animal must be an Animal instance.")
        if not isinstance(description) or not description.strip():
            raise ValueError("description cannot be an empty string.")
        if not isinstance(severity) or not (1 <= severity <= 10):
            raise ValueError("severity must be an integer between 1-10.")
        record = self.__create_health_record(description.strip(), severity, (treatment_notes or "").strip())
        animal.add_health_record(record)
        return f"{self.__name} added health record for {animal.name} - severity of {severity}."