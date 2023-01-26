import sys
import traceback
import twitter
import json
import collections
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import re
import sklearn
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.linear_model import _logistic

from wordcloud import WordCloud
from collections import Counter
from hatesonar import Sonar

import matplotlib.pyplot as plt


api = twitter.Api('nWvH6EPUc9KszZwJhmiU2E10q',
                  'kmbJnDFeBisnZS844uHikHm7sy0A5jCeshTqwUtLGiCCLQooQI',
                  '702741805922697216-KW2aRlNHiUhndiG1FN49fnLNdqBWq9q',
                  'NBpK175Zaz3Ni3EwsSQ7GZCdikIL0u9AackGwHomOV7uL')


nome = sys.argv[1]
cognome = sys.argv[2]


userTokens = []

results = api.GetUsersSearch(nome + " " + cognome)
more_results = api.GetUsersSearch(nome + cognome)

for i in range(len(more_results)):
    results.append(more_results[i])

if(len(results) == 0):
    print("Non ho trovato niente su twitter")
else:
    print("Ho trovato questo su twitter:")



for i in range(len(results)):

    print(results[i])
    

    json_user = json.loads(str(results[i]))
    #print(json_user)
    followers = ""
    verified = ""
    name = ""
    descrizione = ""
    
    imgProfilo = ""
    try:
        followers = '\033[103m' + str(json_user['followers_count']) +  '\033[0m'
    except:
        followers = ""
    try:
        verified = '\033[0;32m' + str(json_user['verified'])+  '\033[0m'
    except:
        verified = '\033[91m' + "FALSE" +    '\033[0m'
    try:
        name = '\033[91m' + json_user['name'] +  '\033[0m'
    except:
        name = ""  
    try:
        descrizione =  json_user['description']

     
    except:
        descrizione = ""  
    try:
        imgProfilo = json_user['profile_image_url']
    except:
        imgProfilo = ""  
    print("[" + str(i)+  "]  NOME = " + name + " DESCRIZIONE = " + descrizione + " FOLLOWERS = " + str(followers) + " VERIFIED = " + verified + " IMMAGINE PROFILO = " + imgProfilo+ "\n")


try:
    if(len(results) != 0):
        selected = input("Seleziona la persona cercata oppure premi Q per continuare\n")

        

        selected_json =  json.loads(str(results[int(selected)]))
        selected_id = int(selected_json["id"])
        
        data = {}
        data['name'] = selected_json["name"]
        try:
            data['description'] = selected_json["description"]
            userTokens.append(data['description'])
        except:
            data['description'] = "Descrizione mancante"
        data['profile_image_url'] = selected_json["profile_image_url"]
        data['current_status'] = selected_json["status"]

        #print(results[int(selected)])

        #print("@@@@@@@@@@@@@@@@@@@@@@@@UserTimeLine:")
        #print(api.GetUserTimeline(selected_id))
        selected_status = api.GetUserTimeline(selected_id, count=1000)
        #retweets = api.GetUserRetweets(selected_id)

        #for i in retweets:
        #    userTokens.append(i)

        statuses = []
        for i in range(len(selected_status)):
            status = selected_status[i]
            json_status = json.loads(str(status))
            userTokens.append(json_status["text"])
        # print("@@@@@@@@@@@@@@@@@@@@@STATUS = " + str(status))
            statuses.append(json_status["text"])

        #print(statuses)
     #   print("TOKENS =  ################################################\n")
    #    print(userTokens)

        sonar = Sonar()
        offensiveLanguageDataset = []
        hateLanguageDataset = []
        
        for i in userTokens:
            #print(i)
            hateData = sonar.ping(i)
            hate_speech = hateData['classes'][0] 
            offensive_language = hateData['classes'][1]
            print(hateData)
            if(hate_speech['confidence'] >=0.39):
                hateLanguageDataset.append(hateData['text'])
                print(hateData)
            if(offensive_language['confidence'] >=0.45):
                offensiveLanguageDataset.append(hateData['text'])
                print(hateData)
            
       #     print(hateData['classes'][0])

        #clean_text_1 = frasi divise in token
        clean_text_1 = [word_tokenize(i) for i in userTokens]

        #clean_text_2 = frasi divise in token ma senza spazi e altre cose strane
        clean_text_2 = []

        #clean_text_3 = applico l'algoritmo di porter
        clean_text_3 = []
         #clean_text_4 = applico lemmatization
        clean_text_4 = []
        #clean_text_5 = tengo solo i nomi -> da fare
        clean_text_5 = []
        fdist = FreqDist()

        for words in clean_text_1:
            clean = []
            for w in words:
                res = re.sub(r'[^\w\s]',"",w)
                res = re.sub('(\s+)(a|an|and|the|we|if|that|a|in|i|http|thing|lot|far|week|use|rt|then)(\s+)', '\1\3', res.lower())
                if res != "":
                    clean.append(res)
            clean_text_2.append(clean)

        port = PorterStemmer()
        stemmer = SnowballStemmer('english')
        
        for words in clean_text_2:
            w = []
            print(str(words) + '\n')
            for word in words:
                if not word in stopwords.words('english'):
                    stemmed = stemmer.stem(word)
                    if stemmed not in ['rt','see','still','go','found','take']:
                        w.append(stemmer.stem(word))
                    
            
            print(str(w) + '\n')
            clean_text_3.append(w)


        lemmatizer = WordNetLemmatizer()
        for words in clean_text_3:
            for word in words:
                clean_text_4.append(lemmatizer.lemmatize(word))
            

       # contro la frequenza dei token
        for word in clean_text_4:
                fdist[word]+= 1

        
       # print(clean_text_4)    
        print("\n################################\n")
        sortedKeywords = sorted(fdist.items(), key=lambda x: x[1])
        sortedKeywords.pop()


        print(sortedKeywords)

        last20KeyWOrdsSorted = sortedKeywords[-70:]

        plt.rc_context({"xtick.major.pad": 10})
        plt.figure(figsize=(20, 10)) 
        plt.xticks(rotation=90)
        plt.bar( *zip(*last20KeyWOrdsSorted))
        plt.savefig('output/img/keywords.png')

        all_words = ' '.join([text[0] for text in sortedKeywords])
        wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)
        plt.figure(figsize=(20, 10))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        plt.title('Random Words')
        plt.savefig('output/img/randomWords.png')

 


        if(len(hateLanguageDataset) > 0):
            word_could_dict = Counter(hateLanguageDataset)
            wordcloud = WordCloud(width=3000, height=700, prefer_horizontal=1).generate_from_frequencies(word_could_dict)

            data['hateLanguage'] = hateLanguageDataset
            plt.figure(figsize=(20, 10))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis('off')
            plt.title('Hate Speech')
            plt.savefig('output/img/hateSpeech.png')

        if(len(offensiveLanguageDataset) > 0):
            word_could_dict = Counter(offensiveLanguageDataset)
            data['offensiveLanguage'] = offensiveLanguageDataset
            wordcloud = WordCloud(width=3000, height=1500, prefer_horizontal=1).generate_from_frequencies(word_could_dict)
            plt.figure(figsize=(20, 10))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis('off')
            plt.title('Offensive Language')
            plt.savefig('output/img/offensive.png')

       
        data['searched_name'] = nome + " " + cognome
        data['statuses'] = statuses


        json_data = json.dumps(data, indent=5)
        #print(json_data)

        # Writing to person.json
        f = open("twitter.json", "w")
        f.write(json_data)
        f.close()


    
        
    else:

        f = open("twitter.json", "w")
        f.write("{}")
        f.close()

except:
    traceback.print_exc()

    f = open("twitter.json", "w")
    f.write("{}")
    f.close()