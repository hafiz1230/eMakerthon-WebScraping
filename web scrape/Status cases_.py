# ------@gROUP 18---------------#
from bs4 import BeautifulSoup
import requests
import numpy as np

######################### R Naught ########################################
page1 = requests.get('http://covid-19.moh.gov.my/terkini').text
soup1 = BeautifulSoup(page1,'html.parser')      #Get page source
rnaught=soup1.findAll("div", {"id" : "custom-2550-particle"} , {"class": "g-content g-particle"})

rnaught=str(rnaught)

rDate = rnaught.split('/kajian-dan-penyelidikan/nilai-r-malaysia">',1)[1]   #Needing Respiratory Assistance Cases
rDate= rDate.split(' <strong><span style="',1)[0]

r0 = rnaught.split('rgb(184, 49, 47);">',1)[1]   #Needing Respiratory Assistance Cases
r0= r0.split('</span></strong></a>',1)[0]

#######################################################
html_text = requests.get('https://kpkesihatan.com/').text
linkFirst = BeautifulSoup(html_text,'html.parser')      #Get page source
link_First=linkFirst.find('h2',class_='posttitle').a['href']

url=link_First   #Latest link covid

page=requests.get(url).text
soup=BeautifulSoup(page,'html.parser')

f = soup.findAll("section",{"class":"entry"})
t = f[0].find("ul")

t=t.text
t=t.replace("\xa0", " ")   ##Remove nbsp

d= soup.findAll("h1",{"class":"title"})  #Get specific code
d=str(d)
d1= d.split('Kenyataan Akhbar KPK ',1)[1]   #ICU Cases
date= d1.split(' – Situasi',1)[0]

nc = t.split('Kes baharu : ',1)[1]     #New Cases
nc1= nc.split(' kes',1)[0]
nc2 = nc1.replace(',', '')
ncFinal = nc2

ac = t.split('Kes aktif : ',1)[1]      #Active cases
ac1= ac.split(' kes',1)[0]
ac2 = ac1.replace(',', '')
acFinal = ac2

nr = t.split('Kes sembuh : ',1)[1]     #Recovery cases
nr1= nr.split(' kes',1)[0]
nr2 = nr1.replace(',', '')
nrFinal = nr2

nd = t.split('Kes kematian : ',1)[1]   #Death cases
nd1= nd.split(' kes',1)[0]
nd2 = nd1.replace(',', '')
ndFinal = nd2

ic = t.split('Kes import : ',1)[1]     #Import cases
ic1= ic.split(' kes',1)[0]
ic2 = ic1.replace(',', '')
icFinal = ic2

lc = t.split('Kes tempatan : ',1)[1]   #Local cases
lc1= lc.split(' kes',1)[0]
lc2 = lc1.replace(',', '')
lcFinal = lc2

icu = t.split('Kes yang memerlukan rawatan di Unit Rawatan Rapi (ICU) : ',1)[1]   #ICU Cases
icu1= icu.split(' kes',1)[0]
icu2 = icu1.replace(',', '')
icuFinal = icu2

rac = t.split('Kes memerlukan bantuan pernafasan : ',1)[1]   #Needing Respiratory Assistance Cases
rac1= rac.split(' kes',1)[0]
rac2 = rac1.replace(',', '')
racFinal = rac2

data0={
    "img":"https://image.flaticon.com/icons/png/128/3522/3522520.png",
    "title": rDate ,
    "detail": r0,
}

data1={
    "img": "https://image.flaticon.com/icons/png/128/3078/3078914.png",
    "title": "Article Date",
    "detail": date,
}

data2={
    "img":"https://t3.ftcdn.net/jpg/02/31/30/12/240_F_231301229_RfYXoVN8sPWnrOoirxLXaiTZ7IBMMpqe.jpg",
    "title":"New Cases",
    "detail": ncFinal,
}

data3={
    "img":"https://t4.ftcdn.net/jpg/04/12/54/85/240_F_412548536_rlGtfA9s26r4tRz1FomqtUh7pCF6z4mh.jpg",
    "title":"Recovery Cases",
    "detail": nrFinal,
}

data4={
    "img":"https://static.vecteezy.com/system/resources/thumbnails/002/207/898/small/raising-influenza-attributable-deaths-rgb-color-icon-vector.jpg",
    "title":"Death Cases",
    "detail":ndFinal ,
}

data5={
    "img":"https://image.flaticon.com/icons/png/128/2600/2600262.png",
    "title":"Active Cases",
    "detail": acFinal,
}

data6={
    "img":"https://image.flaticon.com/icons/png/128/744/744502.png",
    "title":"Import Cases",
    "detail": icFinal,
}

data7={
    "img":"https://image.flaticon.com/icons/png/128/1397/1397897.png",
    "title":"Local Cases",
    "detail": lcFinal,
}

data8={
    "img":"https://image.flaticon.com/icons/png/128/3468/3468070.png",
    "title":"ICU cases",
    "detail": icuFinal ,
}

data9={
    "img":"https://image.flaticon.com/icons/png/128/3140/3140289.png",
    "title":"Needing Respiratory Assistance Cases",
    "detail": racFinal,
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


db.collection("Status Cases").document("0Date").set(data1)   ## Store in firestore
db.collection("Status Cases").document("0Date").update({u'data1':True})   ## Update in firestore

db.collection("Status Cases").document("0rnaught").set(data0)
db.collection("Status Cases").document("0rnaught").update({u'data0':True})

db.collection("Status Cases").document("1New Cases").set(data2)
db.collection("Status Cases").document("1New Cases").update({u'data2':True})

db.collection("Status Cases").document("2Recovery Cases").set(data3)
db.collection("Status Cases").document("2Recovery Cases").update({u'data3':True})

db.collection("Status Cases").document("3Death Cases").set(data4)
db.collection("Status Cases").document("3Death Cases").update({u'data4':True})

db.collection("Status Cases").document("4Active Cases").set(data5)
db.collection("Status Cases").document("4Active Cases").update({u'data5':True})

db.collection("Status Cases").document("5Import Cases").set(data6)
db.collection("Status Cases").document("5Import Cases").update({u'data6':True})

db.collection("Status Cases").document("6Local Cases").set(data7)
db.collection("Status Cases").document("6Local Cases").update({u'data7':True})

db.collection("Status Cases").document("7ICU cases").set(data8)
db.collection("Status Cases").document("7ICU cases").update({u'data8':True})

db.collection("Status Cases").document("8Needing respiratory").set(data9)
db.collection("Status Cases").document("8Needing respiratory").update({u'data9':True})


