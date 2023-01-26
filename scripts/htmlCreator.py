import json
from os import listdir
from os.path import isfile, join

print("Now I generate the .html report....")

# to open/create a new html file in the write mode
# Opening JSON file
f = open('tmp/person.json')
  
# returns JSON object as 
# a dictionary


html_intestation= """<html>
    <head>
    <title>Report</title>
    </head>
    <body>
    <h1>This is what we have found:</h1>
    """


html_images = "<div> <b>We found those images:</b><br>"


html_linkedin = "<div>  <h2>Linekdin</h2><br>"
html_linkedin_jobs = "<b>Jobs</b> <br>"
html_linkedin_education = "<b>Education</b><br>"

try:
    linkedin = json.load(f)
    #print(linkedin)

    text = f.read()
    
    # the html code which will go in the file GFG.html


    nome = ""
    jobtitle = ""
    location = ""
    try:
        nome = linkedin['nome']
    except:
        nome = ""
    try:
        jobtitle = linkedin['jobtitle']
    except:
        jobtitle = ""
    try:
        location = linkedin['location']
    except:
        location = ""



    html_linkedin = "<div>  <h2>Linekdin</h2>" + "<br><b>Personal Informations</b><br> <p> Name= " +  nome +  "</p> Job Title= " + jobtitle + "</p> Location= " + location + "</p> <br>"
    html_linkedin_jobs = "<b>Jobs</b> <br>"
    html_linkedin_education = "<b>Education</b><br>"

    linkedinExperiences = list(linkedin['experience'])



    for i in range(len(linkedinExperiences)):
        locationName = ""
        geoLocationName = ""
        companyName = ""
        description = ""
        try:
            locationName = linkedinExperiences[i]['locationName']
        except:
            locationName = ""
        try:
            geolocationName = linkedinExperiences[i]['geoLocationName'] 
        except:
            geolocationName = ""
        try:
            companyName = linkedinExperiences[i]['companyName']
        except:
            companyName = ""
        try:
            description = linkedinExperiences[i]['description']
        except:
            description = ""

        html_linkedin_jobs += "<p> Location Name= " + locationName + "</p> Geo Location Name= " + geolocationName + "</p> Company Name= " + companyName+ "</p> Description= " + description + "</p><br><br>"


    linkedinEducation = list(linkedin['education'])



    for i in range(len(linkedinEducation)):
        schoolName=""
        fieldOfStudy=""
        try:
            schoolName = linkedinEducation[i]['schoolName']
        except:
                schoolName=""
        try:
            fieldOfStudy  = linkedinEducation[i]['fieldOfStudy'] 
        except:
            fieldOfStudy=""



        html_linkedin_education += "<p>School Name= " + schoolName + "</p> <p>Field of study= " + fieldOfStudy + " </p><br>"
    
except:
    html_linkedin = ""





#print(html)



f = open('tmp/twitter.json')
  
# returns JSON object as 
# a dictionary
twitter = json.load(f)
#print(linkedin)

profileImageUrl = ""
current_status = ""

try:
    html_images += "<img src='"+ twitter['profile_image_url'] + "'>"
except:
    html_images = html_images
try:
    description  = twitter['description']
except:
    description=""
try:
    current_status  = twitter['current_status']['text']
except:
    current_status=""




html_twitter = "<div><h2>Twitter</h2><br><b>Personal Informations</b><br> <p>" + description + "</p> <p>Current Status= " + current_status + "</p>"
html_twitter_statuses = "<br><b>Tweets</b><br>"


try:
    twitterStatuses = list(twitter['statuses'])
except:
    twitterStatuses = []


for i in range(len(twitterStatuses)):
    html_twitter_statuses += "<p> " + twitterStatuses[i] + "</p>"




#INSTAGRAM
f = open('instagramSelectedUser.txt')

#INSTAGRAM
nome = f.read()


instagramImages = []

onlyfiles = [f for f in listdir("output") if isfile(join("output", f))]
for i in range(len(onlyfiles)):
    if(".jpg" in onlyfiles[i]):
        instagramImages.append("output/" + onlyfiles[i])


instaInfo = open("output/" + nome + '_info.json')
instaInfo_json= json.load(instaInfo)


fullname=""
biography=""

try:
    fullname  = instaInfo_json['full_name']
except:
    fullname=""
try:
    biography  = instaInfo_json['biography']
except:
    biography=""

try:
    html_images += "<img src=\'" + instaInfo_json['profile_pic_url_hd'] + "\'>"
except:
    html_images = html_images



html_instagram = "<div><h2>Instagram</h2><br><b>Personal Informations</b><br> <p>Full Name = " + fullname + "</p> <p>Biography = " + biography + "</p>"


html_instagramHashtags = "<br><b>Hashtags:</b><br>"

try:
    instaHashtags = open("output/" + nome + '_hashtags.json')
    instaHashtags_json= json.load(instaHashtags)

    hashtags = instaHashtags_json['hashtags']
    html_instagramHashtags += "<p> " 
    for i in range(len(hashtags)):
        html_instagramHashtags +=  hashtags[i] + "  "
    html_instagramHashtags +="</p>"
except:
    html_instagramHashtags = html_instagramHashtags




try:
    html_instagramAddress = "<br><b>Address found:</b><br>"
    instaAddress = open("output/" + nome + '_addrs.json')
    instaAddress_json= json.load(instaAddress)

    address = instaAddress_json['address']
    for i in range(len(address)):
        html_instagramAddress += "<p> Address = " +  address[i]['address'] + " Time = " + address[i]['time'] + "</p>"
except:
    html_instagramAddress = html_instagramAddress



for i in range(len(instagramImages)):
    html_images += "<img style='max-width: 238px; max-height: 300px;' src='" + instagramImages[i] + "'>"











html = html_intestation + html_images + "</div>" + html_linkedin + html_linkedin_jobs + html_linkedin_education + "</div>" +  html_twitter + html_twitter_statuses + "</div>" + html_instagram + html_instagramAddress + html_instagramHashtags +"</div>" +  "</body></html>"


report = open('output/report.html', 'w')
report.write(html)
  
# close the file
report.close()

