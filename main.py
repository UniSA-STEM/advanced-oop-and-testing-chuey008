'''
File: main.py
Description: This class Main file acts as a demonstration script, creating objects, methods and printing
results.
AAuthor: Emily Chuong
ID: 110448094
Username: chuey008
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Mammal, Bird, Reptile, Other
from enclosure import Enclosure, EnvironmentType
from staff import Staff

def demo():
    """
    Run a short scenario to demonstrate the below:
    1. create animals for Mammal, Bird, Reptile and Other subclasses
    2. create enclosures and compatible animals based on EnvironmentType
    3. create staff and assign responsibilities based on role
    4. demonstrate feeding, cleaning, vet checks, error cases (e.g. moving an animal under treatment)
    """
    # create animals using private state, public API used below
    ellie = Mammal(name="Ellie", species="elephant", age=5, diet="Herbivore")
    peta = Bird(name="Peta", species="parrot", age=2, diet="Omnivore")
    tilly = Reptile(name="Tilly", species="turtle", age=25, diet="Omnivore")
    fred = Other(name="Fred", species="tree frog", age=10, diet="Carnivore")

