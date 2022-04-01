import random
import datetime
import requests

# test out random creation of boolean values
def get_rand_bool():
    """
    Generates random boolean value.

    Generates a random boolean value, used for generating random genders for example population patients.

    Returns
    -------
    Boolean
        1 = Male, 0 = Female
    """
    return bool(random.getrandbits(1))

def get_random_date():
    """
    Generates random date.

    Generates random date between 1930/1/1, and 2020/1/1. Used to generate random birthdates for example population patients.

    Returns
    -------
    DateTime
        Randomly generated datetime object.
    """
    start_date = datetime.date(1930, 1, 1)
    end_date = datetime.date(2020, 1, 1)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def generate_random_icd_code():
    """
    Generates a random ICD code.

    Generates a random ICD code of the format J80.0.

    Returns
    -------
    String
        Randomly generated ICD-code as string.
    """
    import string
    first_letter = random.choice(string.ascii_uppercase)
    first_number = random.randrange(10)
    second_number = random.randrange(10)
    third_number = random.randrange(10)
    
    return '{}{}{}.{}'.format(first_letter, first_number, second_number, third_number)
    
    
def get_random_diagnosis():
    """
    Generates random diagnosis based on code.

    Generates a random ICD diagnosis, based on the value of the provided code. Every valid ICD format code can be supplied. Using the icd10api.com endpoint, a JSON response is generated. Uses the generate_random_icd_code function.

    Returns
    -------
    JSON
        JSON object representation of the data received by the ICD10 API.
    """
    url = 'http://www.icd10api.com/'
    
    payload = {
        'code': generate_random_icd_code()
    }
    response = requests.get(url, params=payload)
    
    # generate new ICD10 codes as long as the given code is invalid
    try:
        while response.json()['Error']:
            payload = {
            'code': generate_random_icd_code()
            }
            response = requests.get(url, params=payload)
    # if 'Error' is not found in the keys, we have valid ICD10 code and can proceed.
    except KeyError:
        return response.json()['Description'].strip().replace(',', '')
    


if __name__ == '__main__':
    # r = get_random_diagnosis()
    # print(r.text)
    diagnosis = get_random_diagnosis()
    print(diagnosis)