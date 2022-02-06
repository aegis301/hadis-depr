import names
import random
from populate_helpers import generate_random_icd_code, get_random_date, get_random_diagnosis

class DummyPatient():
    def __init__(self, *args, **kwargs):
        self.gender = bool(random.getrandbits(1))
        self.kis_id = random.randint(10000000, 99999999)
        if self.gender:
            self.first_name = names.get_first_name(gender='male')
        else:
            self.first_name = names.get_first_name(gender='female')
        self.last_name = names.get_last_name()
        self.date_of_birth = get_random_date()
        self.diagnosis = get_random_diagnosis()

    def insert_data():
        pass


if __name__ == '__main__':
    patients = []
    
    for i in range(0,1000):
        patients.append(DummyPatient())
        print(i,'th iteration, Patient created successfully.')