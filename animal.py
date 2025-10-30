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
    def __init__(self, description, reported_on, severity, treatment_notes):
        """
        Represents a health record in an animal if there is an event.
        All are private to enforce encapsulation and checks to see the validity of HealthRecords to prevent invalid
        records from being entered.
        """
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Description cannot be an empty string.")
        if not isinstance(reported_on, date):
            raise ValueError("Reported on must be a date and time.")
        if not isinstance(severity, int) or not (1 <= severity <=10):
            raise ValueError("Severity must be an integer between 1 and 10.")
        if not isinstance(treatment_notes, str):
            raise ValueError("Treatment notes must be a string.")

        # ensuring internal fields are private
        self.__description = description
        self.__reported_on = reported_on
        self.__severity = severity
        self.__treatment_notes = treatment_notes

    # using @property decorator to transform a method into a getter
    @property
    def description(self):
        # short description of what the health issue or disease or condition is
        return self.__description

    @property
    def report_on(self):
       # date of when the issue was reported
        return self.__reported_on

    @property
    def severity(self):
        # score of severity from 1 (mild) to 10 (critical)
        return self.__severity

    @property
    def treatment_notes(self):
        # notes about the treatment or follow up, could be empty if not severe
        return self.__treatment_notes

    # represents a string for debugging and tests
    def __repr__(self):
        return f"HealthRecord({self.__reported_on.isoformat()},sev={self.__severity}, desc={self.__description})"

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
