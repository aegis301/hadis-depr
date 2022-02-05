import names
import random
from helpers import get_random_date, get_random_diagnosis

class DummyPatient():
    def __init__(self, *args, **kwargs):
        self.gender = bool(random.getrandbits(1))
        if self.gender:
            self.first_name = names.get_first_name(gender='male')
        else:
            self.first_name = names.get_first_name(gender='female')
        self.last_name = names.get_last_name()
        self.date_of_birth = get_random_date()
        self.diagnosis = get_random_diagnosis()
    


def create_patient():
    pass