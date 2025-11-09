'''
File: enclosure.py
Description: This class Enclosures file is used to house the animals, includes attributes like size, environmental type,
and cleanliness level. Should report current status and list of animals inside.
Author: Emily Chuong
ID: 110448094
Username: chuey008
This is my own work as defined by the University's Academic Integrity Policy.
'''

"""
Importing enum.Enum to use to define a closed set of environment types to avoid string typos.
Importing typing.List used for type hints for lists of Animal.
"""
from enum import Enum
from typing import List
from animal import Animal

class EnvrionmentType(Enum):
    """
    Using Enumerate to help with debugging and preventing any invalid environment types.
    """
    AQUATIC = "aquatic"
    SAVANNAH = "savannah"
    DESERT = "desert"
    TROPICAL = "tropical"
    RAINFOREST = "rainforest"
    ARCTIC = "arctic"
    TEMPERATE = "temperate"  # general environment that is able to host a wide range of animals

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
        if not isinstance(environment, EnvironmentType):
            raise TypeError("environment must be a valid EnvironmentType")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")

    def __reduce_cleanliness(self, amount):
        """
        Private helper to reduce the cleanliness level of the enclosure.
        """
        self.__cleanliness = max(0, self.__cleanliness - amount)

    def __compatible_with_environment(self, animal: Animal):
        """
        Private helper to check if the animal is compatible with the environment type in the enclosure.
        Method encapsulates the mapping of animal species to environments.
        Substring based, for additional flexibility - e.g. specific species like "brown bear" and "polar bear"
        """
        a_s = animal.species.lower()
        env = self.__environment
        if env == EnvironmentType.AQUATIC:
            return any(i in a_s for i in ("dolphin", "seal", "penguin", "fish", "sea otter", "turtle"))
        if env == EnvironmentType.SAVANNAH:
            return any(i in a_s for i in ("giraffe", "elephant", "zebra", "ostrich", "red kangaroo", "meerkat"))
        if env == EnvironmentType.DESERT:
            return any(i in a_s for i in ("camel", "scorpion", "dingo", "bearded dragon", "hawk", "cobra"))
        if env == EnvironmentType.TROPICAL:
            return any(i in a_s for i in ("lemur", "green anaconda", "parrot", "gecko", "capybara", "sloth"))
        if env == EnvironmentType.RAINFOREST:
            return any(i in a_s for i in ("tree frog", "toucan", "spider monkey", "harpy eagle", "tiger", "gorilla"))
        if env == EnvironmentType.ARCTIC:
            return any(i in a_s for i in ("polar bear", "arctic fox", "snowy owls", "walrus", "seal", "puffin"))
        if env == EnvironmentType.TEMPERATE:
            # temperate accepts generalists type animal species
            return True
        return False

    # --------------------------- Public Properties ---------------------------
    @property
    def name(self):
        # name of enclosure
        return self.__name

    @property
    def size_sqm(self):
        # area of enclosure in square metres
        return self.__size_sqm

    @property
    def environment(self):
        # environmentType for this enclosure
        return self.__environment

    @property
    def capacity(self):
        # capacity of the enclosure - having only a maximum number of animals allowed as per the size
        return self.__capacity

    @property
    def cleanliness(self):
        # how clean is the enclosure out of 100
        return self.__cleanliness

    def add_animal(self, animal: Animal):
        """
        Adding an animal to an enclosure.
        Conditions include:
            - animal must be an Animal instance
            - animal must not be undergoing treatment
            - enclosure must have free capacity
            - animal must be compatible with the enclosure environment
        Internal checks to validate the above
        Append the current __animal list
        Reduce the cleanliness of the enclosure due to adding another animal to it
        """
        if not isinstance(animal, Animal):
            raise TypeError("animal must be a valid Animal instance.")
        if animal.under_treatment:
            raise ValueError("animal undergoing treatment cannot be placed into an enclosure.")
        if len(self.__animals) >= self.__capacity:
            raise ValueError("enclosure is at full capacity.")
        if not self.__compatible_with_environment(animal):
            raise ValueError(f"{animal.species} is incompatible with {self.__environment} environment.")
        self.__animals.append(animal)
        self.__reduce_cleanliness(5.0)

