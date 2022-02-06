

class DBPopulator():
    def __init__(self, patients) -> None:
        self.patients = patients
        self.engine = from sqlalchemy import create_engine
        