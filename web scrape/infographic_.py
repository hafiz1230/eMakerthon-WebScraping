# ------@gROUP 18---------------#
from bs4 import BeautifulSoup
import requests
import numpy as np
import urllib    ## Save image from image url


page = requests.get('http://covid-19.moh.gov.my/terkini').text
soup = BeautifulSoup(page,'html.parser')      #Get page source

title = soup.findAll("h2",{"class":"p-name"})[0]
title=title.findAll("a",{"class":"u-url"})
t=title[0]
title=t.text

imge= soup.findAll("div",{"class":"list-blog-padding"})[0]
imge=imge.findAll("div")[2]
img=str(imge)

lk = img.split('<img alt="" src="',1)[1]     #New Cases
lk1= lk.split('></div>',1)[0]
moh= "http://covid-19.moh.gov.my/" 
lkFinal = moh + lk1

response = requests.get(lkFinal)  ## Save image from image url
file = open("sample_image.png", "wb")
file.write(response.content)
file.close()

data={

     "image" : "",
     "title" : title
     
}

# ###------------------------------------------------Upload to firebase-------------------------------###
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Singapore')
time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

cred = credentials.Certificate("path.json")   ##Put your json file
firebase_admin.initialize_app(cred)
db=firestore.client()

db.collection("Infographic").document("983").set(data)   ## Store in firestore

