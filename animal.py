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
        This class represents a health record in an animal if there is an event.
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

    def __repr__(self):
        # represents a string for debugging and tests
        return (f"Date = {self.__reported_on.isoformat()}\n "
                f"Severity = {self.__severity}\n"
                f" Description = {self.__description}")

class Animal:
    def __init__(self, name, species, age, diet):
        """
        Initialise an Animal object with name, species, age and dietary attributes.
        Validation init to keep checks centralised
        Using list for an internal history list
        Boolean used to determine whether the animal is undergoing treatment
        """
        self.__validate_init(name, species, age, diet)
        self.__name = name
        self.__species = species.lower()
        self.__age = age
        self.__diet = diet
        self.__health_records: List[HealthRecord] = []
        self.__under_treatment = False

    # --------------------------- Private Helpers ---------------------------
    def __validate_init(self, name, species, age, diet):
        """
        Internal validator to ensure that what is entered is actually what should be entered.
        Completes internal checks.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name cannot be an empty string.")
        if not isinstance(species, str) or not species.strip():
            raise ValueError("species cannot be an empty string.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("age cannot be a negative integer")
        if not isinstance(diet, str) or not diet.strip():
            raise ValueError("diet cannot be an empty string.")

    # --------------------------- Public Properties ---------------------------
    """
    using @property decorator to transform a method into a getter
    """
    @property
    def name(self):
        # name of the animal
        return self.__name

    @property
    def species(self):
        # the species type of the animal in lower case
        return self.__species

    @property
    def age(self):
        # how old the animal is in years
        return self.__age

    @property
    def diet(self):
        # what does the animal eat
        return self.__diet

    @property
    def under_treatment(self):
        # indicates if the animal is undergoing treatment, flagged in their health records with how severe
        # can be cleared by calling clear_treatment
        return self.__under_treatment

    # --------------------------- Behaviour Methods ---------------------------
    def make_sound(self):
        """
        Default sound method for testing.
        Subclasses would be able to override this method
        Keeping it public to let other components call it without accessing internal state
        """
        return f"{self.__name} the {self.__species} makes a sound"

    def eat(self, food: str):
        """
        This will simulate feeding the animal.
        This will need to be a string, cannot be empty.
        Will return a descriptive string for tests.
        """
        if not isinstance(food, str) or not food.strip():
            raise ValueError("Food cannot be an empty string.")
        return f"{self.__name} eats {food.strip()} - diet: {self.__diet}"

    def sleep(self, hours: int = 8):
        """
        This will simulate the animal sleeping.
        Checks to see if the hours are greater than zero.
        """
        if not isinstance(hours, int) or hours <= 0:
            raise ValueError("Hours must be greater than zero.")
        return f"{self.__name} sleeps for {hours} hours."

    # --------------------------- Health Management ---------------------------
    def add_health_record(self, record: HealthRecord):
        """
        Public method to add a HealthRecord to the animal.
        Only accepts HealthRecord objects/instances.
        Delegates to a private helper to update the internal state.
        """
        if not isinstance(record, HealthRecord):
            raise TypeError("Record must be a HealthRecord instance.")
        self.__add_health_record_private(record)

    def __add_health_record_private(self, record: HealthRecord):
        """
        Private helper to store the health record and update the treatment flag.
        For any animal that has a severity of greater than 5 will undergo treatment.
        All records will still be saved and stored after it is cleared.
        """
        self.__health_records.append(record)
        if record.severity >= 5:
            self.__under_treatment = True

    def get_health_records(self):
        """
        Returns a shallow copy of health records to prevent any changes.
        Will be used for testing as the internal list can't be changed.
        """
        return list(self.__health_records)

    def clear_treatment(self):
        """
        This will clear the animal after they have received treatment.
        Health records will still be saved to make sure the animal is recovering
        """
        self.__under_treatment = False

    def __str__(self):
        """
        A summary of the animal on their health for testing and showcasing output.
        """
        status = "Undergoing treatment" if self.__under_treatment else "Healthy"
        return (f"{self.__name} is part of the {self.__species} species\n"
                f"Age: {self.__age}\n"
                f"Diet: {self.__diet}\n"
                f"Health: {status}\n")

# --------------------------- Animal Subclasses ---------------------------
class Mammal(Animal):
    def __init__(self, name, species, age, diet):
        """
        Subclasses need to inherit properly from parent class Animal, using super().__init__() to call HealthRecords.
        """
        super().__init__(name,species, age, diet)

    def make_sound(self):
        """
        Mammal subclass of parent class that inherits from Animal.
        This will override make_sound method, which shows basic polymorphism.
        """
        return f"{self.name} the {self.species} makes a typical mammal sound."

class Reptile(Animal):
    def __init__(self, name, species, age, diet):
        """
        Subclasses need to inherit properly from parent class Animal, using super().__init__() to call HealthRecords.
        """
        super().__init__(name,species, age, diet)

    def make_sound(self):
        """
        Reptile subclass of parent class that inherits from Animal.
        This will override make_sound method, which shows basic polymorphism.
        """
        return f"{self.name} the {self.species} makes a typical reptile sound."

class Bird(Animal):
    def __init__(self, name, species, age, diet):
        """
        Subclasses need to inherit properly from parent class Animal, using super().__init__() to call HealthRecords.
        """
        super().__init__(name,species, age, diet)

    def make_sound(self):
        """
        Bird subclass of parent class that inherits from Animal.
        This will override make_sound method, which shows basic polymorphism.
        """
        return f"{self.name} the {self.species} makes a typical bird sound."

class Other(Animal):
    def __init__(self, name, species, age, diet):
        """
        Subclasses need to inherit properly from parent class Animal, using super().__init__() to call HealthRecords.
        """
        super().__init__(name,species, age, diet)

    def make_sound(self, custom_sound=None):
        """
        Other subclass of parent class that inherits from Animal - animals that don't fit the above category.
        For simplicity.
        This will override make_sound method, which shows basic polymorphism.
        Create a custom sound for the animal.
        """
        if custom_sound:
            return f"{self.name} the {self.species} makes a {custom_sound} sound."
        else:
            return f"{self.name} the {self.species} makes a typical {self.species} sound."