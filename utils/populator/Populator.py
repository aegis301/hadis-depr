class DBPopulator():
    def __init__(self) -> None:
        self.patients = list() # this will be a list of DummyPatients which is a pyrthon object
        
    def get_n_patients(self, n):
        from DummyPatient import DummyPatient
        for i in range(n):
            print('Patient Nr. {} created successfully!'.format(i+1))
            self.patients.append(DummyPatient())
            
    
    def patients_to_db(self):
        Patients.objects.bulk_create()

            
    
    
if __name__ == '__main__':
    
    populator = DBPopulator()

    populator.get_n_patients(3)
    print(populator.patients)
    for patient in populator.patients:
        print(patient.__dict__)

    populator.patients_to_db()
       
    