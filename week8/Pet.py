class Pet:

    def __init__(self,pet_name="undefined", age=0, owner_name="undefined", weight=0.0,num_of_limbes=0):
        #the variable inside __init__ is instance variable
        self._pet_name = pet_name
        self._age = age
        self._owners_name = owner_name
        self._weight = weight
        self._number_of_limbs = num_of_limbes


    @property
    def pets_name(self):
        return self._pet_name

    @pets_name.setter
    def pets_name(self, new_name):
        self._pet_name = new_name

    @property
    def pets_age(self):
        return self._age

    @pets_age.setter
    def pets_age(self,new_age):
        self._age = new_age

    @property
    def pets_owners_name(self):
        return self._owners_name

    @pets_owners_name.setter
    def pets_owners_name(self, new_owners_name):
        self._owners_name = new_owners_name

    @property
    def pets_weight(self):
        return self._weight

    @pets_weight.setter
    def pets_weight(self, new_weight):
        if new_weight < 0:
            raise ValueError
        self._weight = new_weight

    @property
    def number_of_limbs(self):
        return self._number_of_limbs

    @number_of_limbs.setter
    def number_of_limbs(self,new_limbs):
        if new_limbs < 0:
            raise ValueError
        self._number_of_limbs = new_limbs


def print_screen(self):
    print(f"{self._pet_name}, {self._age}, {self._owners_name}")

def main():
    # define a Pet object
    # my_dog is instance attribute or instance variable/attribute
    my_dog = Pet()

    # fill in ONLY SOME of the fields (or attributes) of my_dog

    my_dog.pets_name = "Jerry"
    # print(f"My dog's name is {my_dog.pets_name}")
    my_dog.pets_owners_name = "Carol"
    # print(f"and I am his owner, my name is {my_dog.pets_owners_name}")
    my_dog.pets_age = 10
    # print(f"his age is {my_dog.pets_age}.")

    try:
        my_dog.number_of_limbs = -10
        print("Fail")
    except ValueError as ex:
        print(ex)
    #above is same as
    print(getattr(my_dog,"pets_name"))
    setattr(my_dog,"pets_age", 8)
    print(my_dog.pets_age)


    #your_dog is another instance attribute or instance variable/attribute
    your_dog = Pet()

    your_dog.pets_name = "Tony"
    your_dog.pets_owners_name = "Ryan"
    your_dog.pets_age = 10
    # print(f"My name is {your_dog.pets_owners_name}, my dog's name is {your_dog.pets_name}, and he is {your_dog.pets_age} old.")

    print_screen(my_dog)
    print_screen(your_dog)
    print(my_dog.number_of_limbs)

    print(Pet.__dict__)


if __name__ == "__main__":
    main()