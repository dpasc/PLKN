from bs4 import BeautifulSoup
import pandas as pd
import requests
import os



#Fix this make it so it clicks through the home page
wow_url = "https://www.wowlink.com.au/wps/portal/!ut/p/c1/04_SB8K8xLLM9MSSzPy8xBz9CP0os3izQB8jJydDRwMDA2djA6Mg_zDHsNBgYwN3U6B8pFm8n79RqJuJp6GhhZmroYGRmYeJk0-Yp4G7izEB3eEg-_DrB8kb4ACOBhB5uA3-lmZAG5x8Az1dTIAsZzN9P4_83FT9gtwIg8yAdEUAE_CBXA!!/dl2/d1/L0lDU0lKSWdrbUEhIS9JRFJBQUlpQ2dBek15cXchL1lCSkoxTkExTkk1MC01RncvN182UUwyQkIxQTAwQzE4MDJSNDFSSkNEMTBPMi8xX19fXzY!/?WCM_PORTLET=PC_7_6QL2BB1A00C1802R41RJCD10O2_WCM&WCM_GLOBAL_CONTEXT=/cmgt/wcm/connect/Content%20Library%20-%20WOWLink/wowlink/topic+centre/buyingmarketing/cds/2020+category+development+schedule"
wow_csvlink = "https://www.wowlink.com.au"
file_path = "//home//daman//Projects//plkn//Resources//"


#Get html from site
payload=requests.get(wow_url)
payload=payload.text


wow_soup = BeautifulSoup(payload,"html.parser")

 #Filter throught and build up URL needed for download
hasFound = False
for link in wow_soup.find_all("a"):
        
       if hasFound == False: 
        if link.text == "Download":
            wow_csvlink = wow_csvlink+link.get("href")
            hasFound = True 
        

print(wow_csvlink)


#Download from link
result = requests.get(wow_csvlink, allow_redirects=True)
open(file_path+'wow.xlsx','wb').write(result.content)

