'''
File: enclosure.py
Description: This class Enclosures file is used to house the animals, includes attributes like size, environmental type,
and cleanliness level. Should report current status and list of animals inside.
Author: Emily Chuong
ID: 110448094
Username: chuey008
This is my own work as defined by the University's Academic Integrity Policy.
'''

# will need to import animals

class Enclosure:
    """
    This class represents the physical enclosure in the zoo.
    Will need to have the Animal objects placed in the correct enclosure based on environment, size, cleanliness.
    Restrictions placed on same type of animal species in the same enclosure, environment type needs to be thought.
    Capacity limit based on the size of the enclosure.
    Track cleanliness level (0-100) - reduces when more of the same type of animal is added and restored
    enclosure is cleaned.
    0 = dirty - 100 = fully clean
    All are private attributes to protect any accidental internal changes
    """
    def __init__(self, name, size_sqm, environment, capacity):
        self.__name = name
        self.__size_sqm = size_sqm
        self.__environment = environment
        self.__capacity = capacity
        self.__animals: List[Animal]=[]
        self.__cleanliness = 100  # start fully clean

    # --------------------------- Private Helpers ---------------------------
    def __validate_init(self, name, size_sqm, environment, capacity):
        """
        Internal validator to ensure that what is entered is actually what should be entered.
        Completes internal checks.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name cannot be an empty string.")
        if not isinstance(size_sqm, int) or size_sqm < 0:
            raise ValueError("size_sqm must be a positive integer")
        if not isinstance(environment, str):  # will need to find a way to check for environment type
            raise
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")

