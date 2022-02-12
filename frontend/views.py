import os

from django.shortcuts import render
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import MetaData, Table, create_engine, insert, select
from sqlalchemy.engine.base import Connection

# custom env variable handling
load_dotenv(find_dotenv())
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PWD = os.getenv('POSTGRES_PWD')

def home(request):
    return render(request, 'frontend/home.html')


def forms(request):
    context = {
        'title': 'Forms'
    }
    return render(request, 'frontend/forms.html')


def show_page(request):
    engine = create_engine('postgresql://{}:{}@localhost:5432/hadis'.format(POSTGRES_USER, POSTGRES_PWD))
    
    conn: Connection
    with engine.connect() as conn:
        with conn.begin():
            meta = MetaData(conn)
            table = Table('api_patient', meta, autoload=True)
            stmt = select(table)
            patients = conn.execute(stmt)
            print(patients)
    
    context = {
        'patients': patients,
        'title': 'Show Patients'
    }
    return render(request, 'frontend/show_page.html', context)
