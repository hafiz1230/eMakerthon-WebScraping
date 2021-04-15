# ------@gROUP 18---------------#
from bs4 import BeautifulSoup
import requests
import numpy as np

html_text = requests.get('https://kpkesihatan.com/').text
linkFirst = BeautifulSoup(html_text,'html.parser')      #Get page source
link_First=linkFirst.find('h2',class_='posttitle').a['href']
url=link_First   #Latest link covid

page=requests.get(url).text
soup=BeautifulSoup(page,'html.parser')

f = soup.findAll("section",{"class":"entry"})
t = f[0].find("ul")
d= soup.findAll("h1",{"class":"title"})  #Get specific code
d=str(d)
d1= d.split('Kenyataan Akhbar KPK ',1)[1]   #ICU Cases
date= d1.split(' – Situasi',1)[0]

t=t.text
t=t.replace("\xa0", " ")

nc = t.split('Kes baharu : ',1)[1]     #New Cases
nc1= nc.split(' kes',1)[0]
nc2 = nc1.replace(',', '')
ncFinal = int(nc2)

ac = t.split('Kes aktif : ',1)[1]      #Active cases
ac1= ac.split(' kes',1)[0]
ac2 = ac1.replace(',', '')
acFinal = int(ac2)

nr = t.split('Kes sembuh : ',1)[1]     #Recovery cases
nr1= nr.split(' kes',1)[0]
nr2 = nr1.replace(',', '')
nrFinal = int(nr2)

nd = t.split('Kes kematian : ',1)[1]   #Death cases
nd1= nd.split(' kes',1)[0]
nd2 = nd1.replace(',', '')
ndFinal = int(nd2)

ic = t.split('Kes import : ',1)[1]     #Import cases
ic1= ic.split(' kes',1)[0]
ic2 = ic1.replace(',', '')
icFinal = int(ic2)

lc = t.split('Kes tempatan : ',1)[1]   #Local cases
lc1= lc.split(' kes',1)[0]
lc2 = lc1.replace(',', '')
lcFinal = int(lc2)

icu = t.split('Kes yang memerlukan rawatan di Unit Rawatan Rapi (ICU) : ',1)[1]   #ICU Cases
icu1= icu.split(' kes',1)[0]
icu2 = icu1.replace(',', '')
icuFinal = int(icu2)

rac = t.split('Kes memerlukan bantuan pernafasan : ',1)[1]   #Needing Respiratory Assistance Cases
rac1= rac.split(' kes',1)[0]
rac2 = rac1.replace(',', '')
racFinal = int(rac2)

data={
    
    "Date": date,
    "New Cases" : ncFinal,
    "Active Cases" : acFinal,
    "Recovery Cases" : nrFinal,
    "Death Cases" : ndFinal,
    "Import Cases" : icFinal,
    "Local Cases" : lcFinal,
    "ICU Cases" : icuFinal,
    "Needing Respiratory Assistance Cases" : racFinal
    
}

###------------------------------------------------Upload to firebase-------------------------------###
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

db.collection("Current status cases").document("Current").set(data)
db.collection("Current status cases").document("Current").update({u'data':True})