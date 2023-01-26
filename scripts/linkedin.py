#posso ottenere:
#1) geolocalizzazione
#2) esperienze lavorative
#3) istruzione
import sys
import os
from linkedin_api import Linkedin
from dotenv import load_dotenv

load_dotenv()

LINKEDIN_USERNAME = os.getenv('linkedinUsername')
LINKEDIN_PASSWORD = os.getenv('linkedinPassword')



# Authenticate using any Linkedin account credentials
api = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD,refresh_cookies=True)



nome = sys.argv[1]
cognome = sys.argv[2]


# GET a profile
#search_result = api.search_people(keywords = 'leonardo cagelli')
search_result = api.search_people(keyword_first_name = nome, keyword_last_name = cognome)



print(search_result)

#profile = api.get_profile('leonardo-cagelli-7365ab23a')

#print(profile)

# GET a profiles contact info
# contact_info = api.get_profile_contact_info('Leonardo Cagelli')

# GET 1st degree connections of a given profile
# connections = api.get_profile_connections('1234asc12304')