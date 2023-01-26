import json as j
import xml.etree.cElementTree as e
with open("twitter.json") as json_format_file:
    d = j.load(json_format_file)


r = e.Element("Account")


e.SubElement(r,"name").text = d["name"]
e.SubElement(r,"description").text = d["description"]
e.SubElement(r,"current_status").text = d["current_status"]["text"]

e.SubElement(r,"profileImage").text = d["profile_image_url"]
for status in d["statuses"]:
    #print(status)
    s = e.SubElement(r,"Status")
    e.SubElement(s,"text").text = status

for status in d["offensiveLanguage"]:
    #print(status)
    s = e.SubElement(r,"offensiveLanguage")
    e.SubElement(s,"text").text = status    

try:
    for status in d["hateLanguage"]:
        #print(status)
        s = e.SubElement(r,"hateLanguage")
        e.SubElement(s,"text").text = status    

except:
    print("no offensive")

a = e.ElementTree(r)
a.write("json_to_xml.xml")