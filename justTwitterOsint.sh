read -p 'Nome: ' nome

read -p 'Cognome: ' cognome
echo $nome $cognome

python3 twitterData.py $nome $cognome
python3 twitterXSLTtransofrmation.py
xsltproc twitterXSLTparser.xsl json_to_xml.xml > dest.html
sleep 2
pandoc -o output.md -t gfm-raw_html dest.html
pandoc dest.html -o libro.epub --epub-cover-image copertinaLibro.jpeg --epub-metadata=meta.xml
