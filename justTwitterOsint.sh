read -p 'Nome: ' nome

read -p 'Cognome: ' cognome
echo $nome $cognome

python3 scripts/twitterData.py $nome $cognome
python3 scripts/twitterXSLTtransofrmation.py
xsltproc scripts/twitterXSLTparser.xsl json_to_xml.xml > output/identikit.html
sleep 2
pandoc -o output/identikit.md -t gfm-raw_html output/identikit.html
pandoc output/identikit.html -o output/identikit.epub --epub-cover-image output/img/copertinaLibro.jpeg --epub-metadata=meta.xml
