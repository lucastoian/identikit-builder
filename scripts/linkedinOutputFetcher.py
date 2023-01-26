import json
from linkedin_api import Linkedin
import os
dirname = os.path.dirname(__file__)
personFile = os.path.join(dirname, '../output/tmp/person.json')
outputFile = os.path.join(dirname, '../output/tmp/output.json')

with open(personFile, "w") as outfile:
    outfile.write("")


from dotenv import load_dotenv

load_dotenv()

LINKEDIN_USERNAME = os.getenv('linkedinUsername')
LINKEDIN_PASSWORD = os.getenv('linkedinPassword')

print("LINKEDIN USERNAME = " + LINKEDIN_USERNAME)

# Authenticate using any Linkedin account credentials
api = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD,refresh_cookies=True)

# GET a profile
#search_result = api.search_people(keywords = 'leonardo cagelli')


#carico il file
f = open(outputFile)
text = f.read()
textList = list(text)

#formatto corettamente il json
for i in range(len(textList)):
    if(textList[i]=='\''):
        textList[i] = '\"'


text = ''.join(textList)


#carico le persone trovate su linkedin dentro peopleArray
try:
    peopleArray = json.loads(text)
    print(peopleArray[0])


    #ciclo e stampo tutte le persone

    print("Ho trovato queste persone, seleziona quella più opportuna")

    for i in range(len(peopleArray)):
        print("[" + str(i) + "]" + " -> " + peopleArray[i]["name"] + "  " + peopleArray[i]["jobtitle"] + " residente a: " + peopleArray[i]["location"])


    #chiedo di selezionare una persona
    selected = input("Seleziona la persona cercata oppure premi Q per continuare\n")







    profile = api.get_profile(peopleArray[int(selected)]["public_id"])










    data = {}
    data['nome'] = peopleArray[int(selected)]["name"]
    data['jobtitle'] = peopleArray[int(selected)]["jobtitle"]
    data['location'] = peopleArray[int(selected)]["location"]
    try:
        data['industryName'] = profile["industryName"]
    except:
        data['industryName'] = ""
    data['geoCountryName'] = profile["geoCountryName"]
    data['geoLocation'] = profile["geoLocation"]
    data['experience'] = profile["experience"]
    data['education'] = profile["education"]
    json_data = json.dumps(data, indent=8)



    # Writing to person.json
    with open(personFile, "w") as outfile:
        outfile.write(json_data)
except:
    print("Non ho trovato niente su linkedin!")
