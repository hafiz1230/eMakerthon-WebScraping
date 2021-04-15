# ------@gROUP 18---------------#
from bs4 import BeautifulSoup
import requests
import numpy as np

###################################################################
html_text = requests.get('https://kpkesihatan.com/').text
linkFirst = BeautifulSoup(html_text,'html.parser')      #Get page source
link_First=linkFirst.find('h2',class_='posttitle').a['href']

url=link_First   #Latest link covid

page=requests.get(url).text
soup=BeautifulSoup(page,'html.parser')

f = soup.findAll("figure",{"class":"wp-block-table"})
d= soup.findAll("h1",{"class":"title"})  #Get specific code
d=str(d)
d1= d.split('Kenyataan Akhbar KPK ',1)[1]   #ICU Cases
date= d1.split(' – Situasi',1)[0]
t = f[1].find("table")

table_rows=t.find_all("tr")[1:]   #First row
num_cases={}
for row in table_rows:
    td_symbol=row.find_all('td')[0].text   #First column
    td_cases=row.find_all('td')[1].text  #Second column
    td={}
    sep = '('    #Remove parentheses
    sep1= '\xa0'  #Remove nbsp
    sep2= ' '      #Remove whitespace
    td_cases = td_cases.split(sep, -1)[0]   #Remove parentheses
    td_symbol=td_symbol.split(sep1, -1)[0]   #Remove nbsp
    td_symbol=td_symbol.replace("WP KUALA LUMPUR", "KL")
    td_symbol=td_symbol.replace("WP PUTRAJAYA", "PUTRAJAYA")
    td_symbol=td_symbol.replace("WP LABUAN", "LABUAN")
    td_symbol=td_symbol.split(sep2, -1)[0]     #Remove whitespace
    num_cases[td_symbol]=td_cases
    num_cases= num_cases

# data = {
#     "Article Date": date,    #Store "date" in dict
#     "Selangor": int(num_cases['SELANGOR'].replace(',' , '')),     #Assigned int and remove " , "
#     "Sabah": int(num_cases['SABAH'].replace(',' , '')),
#     "Johor": int(num_cases['JOHOR'].replace(',' , '')),
#     "WP Kuala Lumpur": int(num_cases['KL'].replace(',' , '')),
#     "Negeri Sembilan": int(num_cases['NEGERI'].replace(',' , '')),
#     "Sarawak": int(num_cases['SARAWAK'].replace(',' , '')),
#     "Pulau Pinang": int(num_cases['PULAU'].replace(',' , '')),
#     "Perak":  int(num_cases['PERAK'].replace(',' , '')),
#     "Kedah": int(num_cases['KEDAH'].replace(',' , '')),
#     "Melaka": int(num_cases['MELAKA'].replace(',' , '')),
#     "Kelantan": int(num_cases['KELANTAN'].replace(',' , '')), 
#     "Pahang": int(num_cases['PAHANG'].replace(',' , '')),
#     "Terengganu": int(num_cases['TERENGGANU'].replace(',' , '')),
#     "WP Labuan": int(num_cases['LABUAN'].replace(',' , '')),
#     "WP Putrajaya": int(num_cases['PUTRAJAYA'].replace(',' , '')),
#     "Perlis": int(num_cases['PERLIS'].replace(',' , '')),
#     "Jumlah Keseluruhan": int(num_cases['JUMLAH'].replace(',' , '')),
#   }

data1={    ## Store in json file
    "img": "https://image.flaticon.com/icons/png/128/3078/3078914.png",
    "title": "Article Date",
    "detail": date,
}

data2={
    "img":"https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/32x32/shadow/symbol_sum.png",
    "title":"Total daily cases",
    "detail": num_cases['JUMLAH'].replace(',' , ''),
}

data3={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Flag_of_Johor.svg/50px-Flag_of_Johor.svg.png",
    "title":"Johor",
    "detail": num_cases['JOHOR'].replace(',' , ''),
}

data4={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Flag_of_Kedah.svg/50px-Flag_of_Kedah.svg.png",
    "title":"Kedah",
    "detail": num_cases['KEDAH'].replace(',' , ''),
}

data5={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Flag_of_Kelantan.svg/50px-Flag_of_Kelantan.svg.png",
    "title":"Kelantan",
    "detail": num_cases['KELANTAN'].replace(',' , ''),
}

data6={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Flag_of_Kuala_Lumpur%2C_Malaysia.svg/50px-Flag_of_Kuala_Lumpur%2C_Malaysia.svg.png",
    "title":"Kuala Lumpur",
    "detail": num_cases['KL'].replace(',' , ''),
}

data7={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Flag_of_Labuan.svg/50px-Flag_of_Labuan.svg.png",
    "title":"Labuan",
    "detail": num_cases['LABUAN'].replace(',' , ''),
}

data8={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Flag_of_Malacca.svg/50px-Flag_of_Malacca.svg.png",
    "title":"Melaka",
    "detail": num_cases['MELAKA'].replace(',' , '') ,
}

data9={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Flag_of_Negeri_Sembilan.svg/50px-Flag_of_Negeri_Sembilan.svg.png",
    "title":"Negeri Sembilan",
    "detail": num_cases['NEGERI'].replace(',' , '') ,
}

data10={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Flag_of_Pahang.svg/50px-Flag_of_Pahang.svg.png",
    "title":"Pahang",
    "detail": num_cases['PAHANG'].replace(',' , ''),
}

data11={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Flag_of_Penang_%28Malaysia%29.svg/50px-Flag_of_Penang_%28Malaysia%29.svg.png",
    "title":"Penang",
    "detail": num_cases['PULAU'].replace(',' , ''),
}

data12={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Flag_of_Perak.svg/50px-Flag_of_Perak.svg.png",
    "title":"Perak",
    "detail":num_cases['PERAK'].replace(',' , '') ,
}

data13={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Flag_of_Perlis.svg/50px-Flag_of_Perlis.svg.png",
    "title":"Perlis",
    "detail":num_cases['PERLIS'].replace(',' , '') ,
}

data14={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Flag_of_Putrajaya.svg/50px-Flag_of_Putrajaya.svg.png",
    "title":"Putrajaya",
    "detail": num_cases['PUTRAJAYA'].replace(',' , ''),
}

data15={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Flag_of_Sabah.svg/50px-Flag_of_Sabah.svg.png",
    "title":"Sabah",
    "detail": num_cases['SABAH'].replace(',' , ''),
}

data16={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Flag_of_Sarawak.svg/50px-Flag_of_Sarawak.svg.png",
    "title":"Sarawak",
    "detail": num_cases['SARAWAK'].replace(',' , ''),
}

data17={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Flag_of_Selangor.svg/50px-Flag_of_Selangor.svg.png",
    "title":"Selangor",
    "detail": num_cases['SELANGOR'].replace(',' , ''),
}

data18={
    "img":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Flag_of_Terengganu.svg/50px-Flag_of_Terengganu.svg.png",
    "title":"Terengganu",
    "detail": num_cases['TERENGGANU'].replace(',' , ''),
}


johor1= str(9999-int(num_cases['JOHOR'].replace(',' , '')))              ##Arrange the cases from high to low
kedah1= str(9999-int(num_cases['KEDAH'].replace(',' , '')))
kelantan1=str(9999-int(num_cases['KELANTAN'].replace(',' , '')))
kl1=str(9999-int(num_cases['KL'].replace(',' , '')))
labuan1=str(9999-int(num_cases['LABUAN'].replace(',' , '')))
melaka1=str(9999-int(num_cases['MELAKA'].replace(',' , '')))
negeri1=str(9999-int(num_cases['NEGERI'].replace(',' , '')))
pahang1=str(9999-int(num_cases['PAHANG'].replace(',' , '')))
pulau1=str(9999-int(num_cases['PULAU'].replace(',' , '')))
perak1=str(9999-int(num_cases['PERAK'].replace(',' , '')))
perlis1=str(9999-int(num_cases['PERLIS'].replace(',' , '')))
putrajaya1=str(9999-int(num_cases['PUTRAJAYA'].replace(',' , '')))
sabah1=str(9999-int(num_cases['SABAH'].replace(',' , '')))
sarawak1=str(9999-int(num_cases['SARAWAK'].replace(',' , '')))
selangor1=str(9999-int(num_cases['SELANGOR'].replace(',' , '')))
terengganu1=str(9999-int(num_cases['TERENGGANU'].replace(',' , '')))
jumlah1=str(9999-int(num_cases['JUMLAH'].replace(',' , '')))


###------------------------------------------------Upload to firebase-------------------------------###
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Singapore')   #Zone time. Not include also can
time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

cred = credentials.Certificate("path.json")   ##Put your json file  # json file from firebase
firebase_admin.initialize_app(cred)
db=firestore.client()


db.collection("Daily Cases").document("0").set(data1)   ## Store in firestore
db.collection("Daily Cases").document("0").update({u'data1':True})  ## Update in firestore

db.collection("Daily Cases").document('1').set(data2)
db.collection("Daily Cases").document('1').update({u'data2':True})

db.collection("Daily Cases").document(johor1).set(data3)
db.collection("Daily Cases").document(johor1).update({u'data3':True})

db.collection("Daily Cases").document(kedah1).set(data4)
db.collection("Daily Cases").document(kedah1).update({u'data4':True})

db.collection("Daily Cases").document(kelantan1).set(data5)
db.collection("Daily Cases").document(kelantan1).update({u'data5':True})

db.collection("Daily Cases").document(kl1).set(data6)
db.collection("Daily Cases").document(kl1).update({u'data6':True})

db.collection("Daily Cases").document(labuan1).set(data7)
db.collection("Daily Cases").document(labuan1).update({u'data7':True})

db.collection("Daily Cases").document(melaka1).set(data8)
db.collection("Daily Cases").document(melaka1).update({u'data8':True})

db.collection("Daily Cases").document(negeri1).set(data9)
db.collection("Daily Cases").document(negeri1).update({u'data9':True})

db.collection("Daily Cases").document(pahang1).set(data10)
db.collection("Daily Cases").document(pahang1).update({u'data10':True})

db.collection("Daily Cases").document(pulau1).set(data11)
db.collection("Daily Cases").document(pulau1).update({u'data11':True})

db.collection("Daily Cases").document(perak1).set(data12)
db.collection("Daily Cases").document(perak1).update({u'data12':True})

db.collection("Daily Cases").document(perlis1).set(data13)
db.collection("Daily Cases").document(perlis1).update({u'data13':True})

db.collection("Daily Cases").document(putrajaya1).set(data14)
db.collection("Daily Cases").document(putrajaya1).update({u'data14':True})

db.collection("Daily Cases").document(sabah1).set(data15)
db.collection("Daily Cases").document(sabah1).update({u'data15':True})

db.collection("Daily Cases").document(sarawak1).set(data16)
db.collection("Daily Cases").document(sarawak1).update({u'data16':True})

db.collection("Daily Cases").document(selangor1).set(data17)
db.collection("Daily Cases").document(selangor1).update({u'data17':True})

db.collection("Daily Cases").document(terengganu1).set(data18)
db.collection("Daily Cases").document(terengganu1).update({u'data18':True})

