# IDENTIKIT BUILDER



Identikit builder is an **OSINT** tool used to collect,analyze and run reconnaissance on Twitter, Instagram and Linkedin platforms.



### Installation ⚙️

You will have to install all those dependencies inside the root directory:

`pip3 install linkedin-api~=2.0.0a`

`pip install python-twitter`

`pip install --user -U nltk`

`python3 -m pip install -U matplotlib`

`pip install WordCloud`

`pip install hatesonar`

`pip3 install "scikit_learn==0.22.2.post1"`



Then you have to install Osintagram dependencies:

Inside *Osintagram* folder : `cd Osintagram` you must run this commands:

1) `python3 -m venv venv`
2) `pip install -r requirements.txt`





### Usage 💻

you will have to grand read, write and execute permission to those shell script:

1. `chmode 777 ./osint.sh`
2. `chmode 777 ./justTwitterOsint.sh`



#### Twitter OSINT

	1. Run  `./justTwitterOsint.sh`

The script will build for you one Identikit in three different formats:

- Epub
- Markdown
- Html

You can inspect the identikits inside `./Output/` folder



#### Linkedin + Twitter + Instagram OSINT

If you want to perform *OSINT* on all those three platforms you will have to:

1. provide your Linkedin username and password inside the *.env* file in the root directory
2. provide your Instagram username and password inside ./Osintagram/config/credentials.ini
3. run the shell script: ./Osint.sh

You can inspect the report inside `./Output/report.html`

#####	:warning: :warning: **DANGER** :warning: :warning:

the scraping done on Linkedin and Instagram is not performed through official api but through selenium bot.

There is a really high chance that your Instagram and Linkedin account will be banned after a few attempts. 

*We suggest you to perform only the Twitter OSINT*



