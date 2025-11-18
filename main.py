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
    print()
    print(tilly.sleep(6))  # behaviour method with a validation
    print()
    print(fred.make_sound("erk erk erk"))  # overrides the make_sound with a more specific sound for a tree frog
    print(fred.make_sound())  # if there is not a custom sound the animal makes

    # create an enclosure with explicit EnvironmentTypes to avoid string typos
    savannah = Enclosure("1A - Savannah", 400.0, EnvironmentType.SAVANNAH, 3)
    tropical_dome = Enclosure("1A - Tropical Dome", 60.0, EnvironmentType.TROPICAL, 6)

    # add animals into their compatible enclosures to demo validation and cleanliness of change
    savannah.add_animal(ellie)
    print()
    tropical_dome.add_animal(peta)
    print(savannah.report_status())
    print()
    print(tropical_dome.report_status())
    print()

    # create staff with roles
    zookeeper = Staff("K001", "Rob", "Zookeeper")
    vet = Staff("V001", "Dr Kate", "Veterinarian")

    # assignments - storing a simple reference, name of staff for this model
    zookeeper.assign_animal(ellie)
    zookeeper.assign_enclosure(savannah.name)
    vet.assign_animal(ellie)

    # actions - feeding and cleaning should be done by the zookeeper Rob
    print(zookeeper.feed_animal(ellie, "grass"))
    print()
    print(zookeeper.clean_enclosure(savannah))
    print()

    # vet check - low severity record - does not make as undergoing treatment using below the threshold
    print(vet.perform_health_check(ellie, "a small cut on the front right leg", 3, "Clean and apply ointment."))
    # check health records have been updated
    print(ellie.get_health_records())

    # vet check - high severity record - should set peta undergoing treatment
    print()
    print(vet.perform_health_check(peta, "broken wing", 8, "Splint applied on wing" ))

    # attempt to move an animal undergoing treatment - this should raise an error or be prevented altogether
    try:
        tropical_dome2 = Enclosure("2A - Tropical Dome 2", 40.0, EnvironmentType.TROPICAL, 2)
        tropical_dome2.add_animal(peta)  # peta is undergoing treatment -> ValueError expected
    except Exception as e:
        print("Error - unable to move animal undergoing treatment:", e)
    print()

    # demonstrate removal of an animal from enclosure and return object usage
    removed = savannah.remove_animal("Ellie")
    print(f"Removed {removed.name} from {savannah.name}")
    print(savannah.report_status())
    print()

    # final printed reports to summarise the zoo state
    print("Final reports:")
    print(ellie)
    print(peta)
    print("Health records for Peta:")
    print(peta.get_health_records())

if __name__ == "__main__":
    demo()

