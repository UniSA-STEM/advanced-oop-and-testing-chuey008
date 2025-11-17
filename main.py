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

    # demonstrate polymorphism through each subclass, which will override make_sound
    print(ellie)  # uses Animal.__str__ which read from the public properties
    print(peta.make_sound())  # makes a bird specific sound
    print(tilly.sleep(6))  # behaviour method with a validation
    print(fred.make_sound("erk erk erk"))  # overrides the make_sound with a more specific sound for a tree frog

    # create an enclosure with explicit EnvironmentTypes to avoid string typos
    savannah = Enclosure(name="1A - Savannah", size_sqm=400.0, environment=EnvironmentType.SAVANNAH, capacity=3)
    aviary = Enclosure(name="1A - Aviary", size_sqm=60.0, environment=EnvironmentType.TROPICAL, capacity=6)

    # add animals into their compatible enclosures to demo validation and cleanliness of change
    savannah.add_animal(ellie)
    aviary.add_animal(peta)
    print(savannah.report_status())
    print(aviary.report_status())

    # create staff with roles
    rob = Staff(staff_id="K001", name="Rob", role="zookeeper")
    dr_kate = Staff(staff_id="V001", name="Dr Kate", role="veterinarian")

    # assignments - storing a simple reference, name of staff for this model
    rob.assign_animal(ellie)
    rob.assign_enclosure(savannah.name)
    dr_kate.assign_animal(ellie)

    # actions - feeding and cleaning should be done by the zookeeper Rob
    print(rob.feed_animal(ellie, "grass"))
    print(rob.clean_enclosure(savannah))

    # vet check - low severity record - does not make as undergoing treatment using below the threshold
    print(dr_kate.perform_health_check(ellie, "a small cut on the front right leg", severity=3, treatment_notes="Clean and apply ointment."))
    print(ellie.get_health_records())  # prints out a list of HealthRecord objects

    # vet check - high severity record - should set peta undergoing treatment
    print(dr_kate.perform_health_check(peta, "broken wing", severity=8, ))

    # attempt to move an animal undergoing treatment - this should raise an error or be prevented altogether
    try:
        aviary2 = Enclosure(name="2A - Aviary", size_sqm=40.0, environment=EnvironmentType.TROPICAL, capacity=2)
        aviary2.add_animal(peta)  # peta is undergoing treatment -> ValueError expected
    except Exception as e:
        print("Error - unable to move animal undergoing treatment:", e)



