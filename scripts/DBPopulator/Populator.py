from scripts.DBPopulator.DummyPatient import MongoDummyPatient
from api.models import Patient

class PostgresDBPopulator():
    def __init__(self) -> None:
        import os
        from dotenv import load_dotenv, find_dotenv

        # custom env variable handling
        load_dotenv(find_dotenv())
        POSTGRES_USER = os.getenv('POSTGRES_USER')
        POSTGRES_PWD = os.getenv('POSTGRES_PWD')
        
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        
        self.patients = list() # this will be a list of DummyPatients which is a pyrthon object
        self.engine = create_engine('postgresql://{}:{}@localhost:5432/hadis'.format(POSTGRES_USER, POSTGRES_PWD))
        self.Session = sessionmaker(self.engine)
        
    def get_n_patients(self, n):
        from .DummyPatient import DummyPatient
        for i in range(n):
            print('Patient Nr. {} created successfully!'.format(i+1))
            self.patients.append(DummyPatient())
            
    
    def patients_to_db(self):
        from sqlalchemy import Table, MetaData, insert
        from sqlalchemy.engine.base import Connection
        
        conn: Connection
        with self.engine.connect() as conn:
            with conn.begin():
                meta = MetaData(conn)
                table = Table('api_patient', meta, autoload=True)
                stmt = insert(table)
                payload = [patient.__dict__ for patient in self.patients]
                print('This is the payload:', payload)
                result_proxy = conn.execute(stmt, payload)
                print('Inserted {} rows.'.format(result_proxy.rowcount))
             
             
class MongoDBPopulator():
    def __init__(self) -> None:
        from mongoengine import connect
        
        self.patients = list()
        self.client = connect(host="mongodb://127.0.0.1/hadis")
        
    def get_n_patients(self, n):
        from .DummyPatient import MongoDummyPatient
        from .populate_helpers import get_random_diagnosis, get_random_date
        import random
        import names
         
        for i in range(n):
            self.patients.append(
                Patient(
                    gender = bool(random.getrandbits(1)),
                    kis_id = random.randint(10000000, 99999999),
                    last_name = names.get_last_name(),
                    date_of_birth = get_random_date(),
                    main_diagnosis = get_random_diagnosis()
                )
            )
            if self.patients[i].gender:
                self.patients[i].first_name = names.get_first_name(gender='male')
            else:
                self.patients[i].first_name = names.get_first_name(gender='female')
            print(f"{i+1}th Patient created succesfully!")
            
    def patients_to_db(self):
        Patient.objects.bulk_create(self.patients)
        # print(f"{patient.last_name} successfully added to the database")
    
    
if __name__ == '__main__':
    
    populator = PostgresDBPopulator()

    populator.get_n_patients(1)
    print(populator.patients)
    for patient in populator.patients:
        print(patient.__dict__)

    populator.patients_to_db()
    
    # im done
       
    