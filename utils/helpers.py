import random
import datetime
import requests

# test out random creation of boolean values
def get_rand_bool():
    return bool(random.getrandbits(1))

def get_random_date():
    start_date = datetime.date(1930, 1, 1)
    end_date = datetime.date(2020, 1, 1)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def get_random_diagnosis():
    pass
    

if __name__ == '__main__':
    pass
    