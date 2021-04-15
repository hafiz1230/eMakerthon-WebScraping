# ------@gROUP 18---------------#
from bs4 import BeautifulSoup
import requests
 
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

t1 = f[0].find("table")

table_rows1=t1.find_all("tr")[1:]   #First row
cluster_num={}
cluster_states={}
cluster_cat={}
for row in table_rows1:
    td_num=row.find_all('td')[0].text         #First column
    td_cluster=row.find_all('td')[1].text     #Second column
    td_states=row.find_all('td')[2].text      #Third column
    td_cat=row.find_all('td')[3].text         #Fourth column
    td={}
    cluster_num[td_num]="Kluster " + td_cluster
    cluster_states[td_num]="Negeri: " + td_states
    cluster_cat[td_num]="Kategori kluster: " + td_cat

data0={
    "header":"Date",
    "title":"Article Date",
    "detail": date,
}

data1={
    "header":cluster_states['1'],
    "title":cluster_num['1'],
    "detail": cluster_cat['1'] ,
}

data2={
    "header":cluster_states['2'],
    "title":cluster_num['2'],
    "detail": cluster_cat['2'] ,
}

data3={
    "header":cluster_states['3'],
    "title":cluster_num['3'],
    "detail": cluster_cat['3'] ,
}

data4={
    "header":cluster_states['4'],
    "title":cluster_num['4'],
    "detail": cluster_cat['4'] ,
}

data5={
    "header":cluster_states['5'],
    "title":cluster_num['5'],
    "detail": cluster_cat['5'] ,
}

data6={
    "header":cluster_states['6'],
    "title":cluster_num['6'],
    "detail": cluster_cat['6'] ,
}

data7={
    "header":cluster_states['7'],
    "title":cluster_num['7'],
    "detail": cluster_cat['7'] ,
}

data8={
    "header":cluster_states['8'],
    "title":cluster_num['8'],
    "detail": cluster_cat['8'] ,
}

data9={
    "header":cluster_states['9'],
    "title":cluster_num['9'],
    "detail": cluster_cat['9'] ,
}

data10={
    "header":cluster_states['10'],
    "title":cluster_num['10'],
    "detail": cluster_cat['10'] ,
}

data11={
    "header":cluster_states['11'],
    "title":cluster_num['11'],
    "detail": cluster_cat['11'] ,
}

data12={
    "header":cluster_states['12'],
    "title":cluster_num['12'],
    "detail": cluster_cat['12'] ,
}

data13={
    "header":cluster_states['13'],
    "title":cluster_num['13'],
    "detail": cluster_cat['13'] ,
}

data14={
    "header":cluster_states['14'],
    "title":cluster_num['14'],
    "detail": cluster_cat['14'] ,
}

data15={
    "header":cluster_states['15'],
    "title":cluster_num['15'],
    "detail": cluster_cat['15'] ,
}

# data16={
#     "header":cluster_states['16'],
#     "title":cluster_num['16'],
#     "detail": cluster_cat['16'] ,
# }

# data17={
#     "header":cluster_states['17'],
#     "title":cluster_num['17'],
#     "detail": cluster_cat['17'] ,
# }

# data18={
#     "header":cluster_states['18'],
#     "title":cluster_num['18'],
#     "detail": cluster_cat['18'] ,
# }

# data19={
#     "header":cluster_states['19'],
#     "title":cluster_num['19'],
#     "detail": cluster_cat['19'] ,
# }

# data20={
#     "header":cluster_states['20'],
#     "title":cluster_num['20'],
#     "detail": cluster_cat['20'] ,
# }

# data21={
#     "header":cluster_states['21'],
#     "title":cluster_num['21'],
#     "detail": cluster_cat['21'] ,
# }

# data22={
#     "header":cluster_states['22'],
#     "title":cluster_num['22'],
#     "detail": cluster_cat['22'] ,
# }




# print(data)
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

db.collection("Cluster").document("0").set(data0)   ## Store in firestore
db.collection("Cluster").document("0").update({u'data0':True})   ## Update in firestore

db.collection("Cluster").document('1').set(data1)
db.collection("Cluster").document('1').update({u'data1':True})

db.collection("Cluster").document('2').set(data2)
db.collection("Cluster").document('2').update({u'data2':True})

db.collection("Cluster").document('3').set(data3)
db.collection("Cluster").document('3').update({u'data3':True})

db.collection("Cluster").document('4').set(data4)
db.collection("Cluster").document('4').update({u'data4':True})

db.collection("Cluster").document('5').set(data5)
db.collection("Cluster").document('5').update({u'data5':True})

db.collection("Cluster").document('6').set(data6)
db.collection("Cluster").document('6').update({u'data6':True})

db.collection("Cluster").document('7').set(data7)
db.collection("Cluster").document('7').update({u'data7':True})

db.collection("Cluster").document('8').set(data8)
db.collection("Cluster").document('8').update({u'data8':True})

db.collection("Cluster").document('9').set(data9)
db.collection("Cluster").document('9').update({u'data9':True})

db.collection("Cluster").document('10').set(data10)
db.collection("Cluster").document('10').update({u'data10':True})

db.collection("Cluster").document('11').set(data11)
db.collection("Cluster").document('11').update({u'data11':True})

db.collection("Cluster").document('12').set(data12)
db.collection("Cluster").document('12').update({u'data12':True})

db.collection("Cluster").document('13').set(data13)
db.collection("Cluster").document('13').update({u'data13':True})

db.collection("Cluster").document('14').set(data14)
db.collection("Cluster").document('14').update({u'data14':True})

db.collection("Cluster").document('15').set(data15)
db.collection("Cluster").document('15').update({u'data15':True})

# db.collection("Cluster").document('16').set(data16)
# db.collection("Cluster").document('16').update({u'data16':True})

# db.collection("Cluster").document('17').set(data17)
# db.collection("Cluster").document('17').update({u'data17':True})

# db.collection("Cluster").document('18').set(data18)
# db.collection("Cluster").document('18').update({u'data18':True})

# db.collection("Cluster").document('19').set(data19)
# db.collection("Cluster").document('19').update({u'data19':True})

# db.collection("Cluster").document('20').set(data20)
# db.collection("Cluster").document('20').update({u'data20':True})

# db.collection("Cluster").document('21').set(data21)
# db.collection("Cluster").document('21').update({u'data21':True})

# db.collection("Cluster").document('22').set(data22)
# db.collection("Cluster").document('22').update({u'data22':True})