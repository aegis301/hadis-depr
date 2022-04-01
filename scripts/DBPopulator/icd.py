import requests
def get_icd_token():
    """
    Deprecated for now, have to look up ICD10 API if needed
    """
    import os
    from dotenv import load_dotenv, find_dotenv

    
    load_dotenv(find_dotenv())
    ICD_CLIENT_ID = os.getenv('ICD_CLIENT_ID')
    ICD_CLIENT_SECRET = os.getenv('ICD_CLIENT_SECRET')
    scope = 'icdapi_access'
    grant_type = 'client_credentials'
    token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
    
    
    payload = {
        'client_id': ICD_CLIENT_ID,
        'client_secret': ICD_CLIENT_SECRET,
        'scope': scope,
        'grant_type': grant_type
    }
    
    
    response = requests.post(token_endpoint, data=payload).json()
    token = response['access_token']
    return token

def get_random_icd_response():
    token = get_icd_token()
    
    url = 'https://id.who.int/icd/schema/code/j18.9'
    
    headers = {
        'Authorization': 'Bearer '+token,
        'Accept': 'application/json',
        'Accept-Language': 'en',
        'API-Version': 'v2'
    }
    
    response = requests.get(url, headers=headers)
    return response