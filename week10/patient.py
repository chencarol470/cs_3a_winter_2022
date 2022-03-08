class Patient():
    """ OOP project development - phase 1 (framework)"""
    # class ("static") intended constants
    ORIGINAL_DEFAULT_NAME = "(no name)"
    ORIGINAL_DEFAULT_ID = 0
    ORIGINAL_DEFAULT_TEMPERATURE = 98.6

    MIN_STR_LEN = 2
    MAX_STR_LEN = 40
    MIN_ID = 0
    MAX_ID = 9999
    MIN_TEMP = 88.
    MAX_TEMP = 111.
    ALARM_TEMP = 103.5

    # class attributes that will change over time
    default_name = ORIGINAL_DEFAULT_NAME
    default_id = ORIGINAL_DEFAULT_ID
    default_temperature = ORIGINAL_DEFAULT_TEMPERATURE

    # initializer method --------------------
    def __init__(self, name=None, patient_id=None, temperature=None):
        # set the defaults / repar mutable defaults
        if name is None:
            name = self.default_name
        if patient_id is None:
            patient_id = self.default_id
        if temperature is None:
            temperature = self.default_temperature

        # instance attributes - remember that these "assignment" are calling\
        # the setter
        try:
            self._name = name  # this name is refer to the setter name
        except ValueError:
            self._name = self.default_name

        try:
            self._patient_id = patient_id  # the patient_id is refer to setter of patient_id
        except ValueError:
            self._patient_id = self.default_id

        try:
            self._temperature = temperature  # the temperature is refer to the setter of temperature
        except ValueError:
            self._temperature = self.default_temperature

    # getters --------------------------------------------------------------
    @property
    def name(self):
        return self._name

    @property
    def patient_id(self):
        return self._patient_id

    @property
    def temperature(self):
        return self._temperature

    # setters ---------------------------------------------------------------
    @name.setter
    def name(self, name):
        if not self.valid_name(name):
            raise ValueError
        self._name = name

    @patient_id.setter
    def patient_id(self, patient_id):
        if not self.valid_id(patient_id):
            raise ValueError
        self._patient_id = patient_id

    @temperature.setter
    def temperature(self, temperature):
        if not self.valid_temp(temperature):
            raise ValueError
        self._temperature = temperature

    # output method -----------------------------------------------------
    def display(self, client_intro_str="---PATIENT DATA---"):
        print(self.to_string(client_intro_str))

    # instance helper -------------------------------------------------
    def to_string(self, optional_title="----------"):
        if not self.valid_string(optional_title):  # placeholder for real test
            optional_title = "----------"
        ret_str = (f"{optional_title}\n                   name: {self.name}"
                   f"\n                     id: {self.patient_id}"
                   f"\n                   temp: {self.temperature}(F)")
        if self.temperature >= self.ALARM_TEMP:
            ret_str += "\n          ***urgent: attend immediately"
        return ret_str

    def __str__(self):
        return self.to_string()

    # static and class helper ------------------------------------
    @classmethod
    def valid_name(cls, str_to_test):
        if type(str_to_test) != str or not \
                cls.MIN_STR_LEN <= len(str_to_test) <= cls.MAX_STR_LEN:
            return False
        return True

    @classmethod
    def valid_id(cls, id_to_test):
        if type(id_to_test) != int or not \
                cls.MIN_ID <= id_to_test <= cls.MAX_ID:
            return False
        return True

    @classmethod
    def valid_temp(cls, temp_to_test):
        if type(temp_to_test) != float and type(temp_to_test) != int or not \
                cls.MIN_TEMP <= temp_to_test <= cls.MAX_TEMP:
            return False
        return True

    @staticmethod
    def valid_string(test_str):
        if test_str != str:
            return False
        return True

    # class setter and getters ---------------------------------------
    @classmethod
    def set_default_id(cls, new_default_id):
        if not cls.valid_id(new_default_id):
            raise ValueError
        cls.default_id = new_default_id

    @classmethod
    def set_default_name(cls, new_default_name):
        if not cls.valid_name(new_default_name):
            raise ValueError
        cls.default_name = new_default_name

    @classmethod
    def set_default_temp(cls, new_default_temp):
        if not cls.valid_temp(new_default_temp):
            raise False
        cls.default_temperature = new_default_temp

#
# #  client ---------------------------------------------------------------------
#
def main():
    # ### main functions ------------------------------------
    """ oop project development - phase 3 (naked main) """

    def get_patient_id():
        """ get id in the form of a string, then convert to int and return """
        string_in = input("What's the patient's id #? ")
        patient_id = int(string_in)
        return patient_id

    def get_patient_name():
        """ get name in the form of a string and return """
        string_in = input("What's the patient's name? ")
        return string_in

    def get_patient_temp():
        """ get id in the form of a string, then convert to float and return """
        string_in = input("What's the patient's temperature? ")
        temp = float(string_in)
        return temp

    # instantiate two Patients
    # person1 = Patient()
    # person2 = Patient()
    person3 = Patient()

    # # get the info for patient #1
    # print("\nPatient #1 ---")
    # user_id = get_patient_id()
    # user_name = get_patient_name()
    # user_temp = get_patient_temp()
    #
    # # set patient #1
    # try:
    #     person1.name = user_name
    # except ValueError:
    #     print("Error in patient name: Invalid length.")
    # try:
    #     person1.patient_id = user_id
    # except ValueError:
    #     print("Error in patient id: not int or out-of-range. ")
    # try:
    #     person1.temperature = user_temp
    # except ValueError:
    #     print("Error in patient temp: not float or out-of-range. ")
    #
    # # get the info for patient #2:
    # print("\nPatient #2 ---")
    # user_id = get_patient_id()
    # user_name = get_patient_name()
    # user_temp = get_patient_temp()
    #
    # # set patient #2:
    # try:
    #     person2.name = user_name
    # except ValueError:
    #     print("Error in patient name: Invalid length.")
    # try:
    #     person2.patient_id = user_id
    # except ValueError:
    #     print("Error in patient id: not int or out-of-range. ")
    # try:
    #     person2.temperature = user_temp
    # except ValueError:
    #     print("Error in patient temp: not float or out-of-range. ")
    # # let's "see" whether we got the correct input
    # print(f"\nPatient 1: {user_name} id: {user_id} temp: {user_temp}")
    #
    # # find the more urgent patient
    # if person1.temperature > person2.temperature:
    #     first = person1
    #     second = person2
    # else:
    #     first = person2
    #     second = person1
    #
    # # display results
    # first.display("Patient with higher temperature: ")
    # second.display("Patient with lower temperature: ")
    user_name = get_patient_name()
    user_id = get_patient_id()
    user_temp = get_patient_temp()

    try:
        person3.name = user_name
    except ValueError:
        print("Error value on name: Invalid length")
    try:
        person3.patient_id = user_id
    except ValueError:
        print("Error value on id: not int or out_of_range.")
    try:
        person3.temperature = user_temp
    except ValueError:
        print("Error value on temp: not float or out_of_range")

    person3.display()



if __name__ == "__main__":
    main()
