import json
from os import listdir
import os
from os.path import isfile, join
onlyfiles = [f for f in listdir("output") if isfile(join("output", f))]
#print(onlyfiles)


#Ciclo su tutti i file e mi apro gli _info


users = []

for i in range(len(onlyfiles)):
    userJson = {}
    if("_info" in onlyfiles[i]):
        print(onlyfiles[i])
        f = open("output/"+onlyfiles[i])
        user = json.load(f)
        userJson['name'] = user['full_name']
        userJson['biography'] = user['biography']
        userJson['profileImage'] = user['profile_pic_url_hd']
        users.append(userJson)
        print("[" + str(i) + "] "+ "Username = " + onlyfiles[i].split("_")[0] + " " + str(userJson))

#print(json.dumps(users))






#chiedo di selezionare una persona
selected = input("Seleziona la persona cercata\n")

os.environ["instaUser"] = onlyfiles[int(selected)].split("_")[0]

print(os.environ["instaUser"])

f = open("instagramSelectedUser.txt", "w")
f.write(onlyfiles[int(selected)].split("_")[0])
f.close()






