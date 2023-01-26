<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl"
>
  <xsl:output method="html" indent="yes"/>
  <xsl:template match="/">
    <html>
      <head>
      </head>
      <body>
            <div style="display:flex; justify-content:center">
                <img>
                    <xsl:attribute name="src">
                        <xsl:value-of select="Account/profileImage"/>
                    </xsl:attribute>
                </img>

                <h1>Search results for <xsl:value-of select="Account/name" /> on twitter</h1>
            </div>

            <ul>
                <li> <p>Description: <xsl:value-of select="Account/description"/></p>    </li>
                <li>      <p>Current status: <xsl:value-of select="Account/current_status"/></p>    </li>
            </ul>

            <div style="max-width: 1000px;margin:auto;    max-width: 600px;margin-top: 20px!important;    display: flex;
            flex-direction: column;    height: 592px; overflow:hidden; text-align: center;
            justify-content: center;">
                <p>Twitter Open Source Intelligence (OSINT) refers to the process of gathering information from publicly available sources, such as Twitter, for the purpose of intelligence gathering, research, or investigations.</p>
                <p>This can include collecting data on individuals, organizations, or events, analyzing trends and patterns, and identifying connections between different pieces of information.</p>
                <p>Tools such as search engines, data mining software, and social media monitoring platforms can be used to collect and analyze data from Twitter and other social media platforms.</p>
                <p>However, it's important to consider the ethical and legal implications of using social media for OSINT, as well as the potential for inaccuracies or biases in the information collected.</p>
                <p style="    margin-bottom: 0;">On the next pages you can find out what we have found about <span>  <xsl:value-of select="Account/name"/></span> on twitter </p> 
                <img style="  width: 100%;"  src="output/img/randomWords.png"></img>
            </div>
   
            


            <div style=" max-width: 1000px;margin:auto; page-break-before:always; height:100%;margin-top:0!important; margin-bottom:0!important;">
                <h2 style="text-align:center;    background-color: #a6d5ff;margin-bottom: 0;">Last 400 status:</h2>
                <img style="  height:40%;  width: 100%;"  src="output/img/keywords.png"></img>
                <div style=" height: 50%;                overflow:auto; padding:40px;background-color: aliceblue; padding-top:0!important; padding-bottom:0!important   ">
                    <xsl:for-each select="Account/Status">
                        <p><xsl:value-of select="text"/></p>
                        <hr></hr>
                    </xsl:for-each>
                </div>
            </div>



            <div style=" max-width: 1000px;margin:auto;  height:100%; margin-top:0!important; margin-bottom:0!important;">
                <h2 style="text-align:center;    background-color: #ff4e4e;margin-bottom: 0;margin-top:0!important;">Offensive language detected:</h2>
                <img style=" height:40%;    width: 100%;" src="output/img/offensive.png"></img>
                <div style="height: 50%;                overflow:auto; padding:40px;background-color: #ffedef; padding-top:0!important;   padding-bottom:0!important ">
                    <xsl:for-each select="Account/offensiveLanguage">
                        <p><xsl:value-of select="text"/></p>
                        <hr></hr>
                    </xsl:for-each>
                </div>
            </div>

            <br></br>

            <div style=" max-width: 1000px;margin:auto;  height:100%;margin-top:0; margin-bottom:0;">
                <h2 style="text-align:center;    background-color: #ff4e4e;margin-bottom: 0;">Hate language detected:</h2>
                <img style=" height:40%;    width: 100%;" src="output/img/hateSpeech.png"></img>
                <div style=" height: 80%;                overflow:auto; padding:40px;background-color: #ffedef; padding-top:0!important;  padding-bottom:0!important  ">
                    <xsl:for-each select="Account/hateLanguage">
                        <p><xsl:value-of select="text"/></p>
                        <hr></hr>
                    </xsl:for-each>
                </div>
            </div>
           
           
      
            

      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>