read -p 'Nome: ' nome

read -p 'Cognome: ' cognome
echo $nome $cognome

space=" "


rm output/*.png -v
rm output/*.html -v
rm output/*.md -v
rm output/*.epub -v
rm output/tmp/* -v
touch output/tmp/person.json

#linkedind 

python3 scripts/linkedin.py $nome $cognome > output/tmp/output.json
python3 scripts/linkedinOutputFetcher.py

#twitter

python3 scripts/twitterData.py $nome $cognome
python3 scripts/twitterXSLTtransofrmation.py
xsltproc scripts/twitterXSLTparser.xsl json_to_xml.xml > output/identikit.html
sleep 2
pandoc -o output/identikit.md -t gfm-raw_html output/identikit.html
pandoc output/identikit.html -o output/identikit.epub --epub-cover-image output/img/copertinaLibro.jpeg --epub-metadata=meta.xml


#Osintgram

#python3 Osintgram/main.py $nome$cognome -C --json --command info
#sleep 8
#python3 Osintgram/main.py $nome.$cognome --json --command info
#sleep 7
#python3 Osintgram/main.py $nome_$cognome --json --command info


#python3 scripts/instagramOutputFetcher.py

#instaUser=`cat instagramSelectedUser.txt`

#echo "hai selezionato " $instaUser


 #               sleep 5
  #              python3 Osintgram/main.py $instaUser --json --command addrs
   #             sleep 6
    #            python3 Osintgram/main.py $instaUser--json --command hashtags
     #           sleep 3
      #          python3 Osintgram/main.py $instaUser --json --command photos



python3 scripts/htmlCreator.py

