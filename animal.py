'''
File: animal.py
Description: This class Animal file allows for the creation and management of animals, with attributes such as
name, species, age, and dietary needs. Animals are categorised by type and capable of performing basic actions.
Author: Emily Chuong
ID: 110448094
Username: chuey008
This is my own work as defined by the University's Academic Integrity Policy.
'''

# Imports are used to show a timestamp of the health events and records and typing to do checks within Health
from datetime import date
from typing import List

class HealthRecord:
    def __init__(self, description, reported_on, severity, treatment):
        """
        Represents a health record in an animal if there is an event.
        All are private to enforce encapsulation and checks to see the validity of  to prevent invalid
        records from being entered.
        """
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Description cannot be an empty string.")
        self.description =

class Animal:
    def __init__(self, name, species, age, diet):
        """
        Initialise an Animal object with name, species, age and dietary attributes.
        """
        self.__validate_init(name, species, age, diet)
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
