from .DBPopulator.Populator import PostgresDBPopulator
# if mongo is selected use mongo populator

# check installed_apps for the same reason
def run():
    
    populator = PostgresDBPopulator()
    populator.get_n_patients(100)
    print(populator.patients)
    populator.patients_to_db()
    
