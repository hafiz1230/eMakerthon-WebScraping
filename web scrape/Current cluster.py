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
    cluster_num[td_num]=td_cluster
    cluster_states[td_num]=td_states
    cluster_cat[td_num]=td_cat

data={
     "Article Date": date,    #Store "date" in dict
     "Cluster name1": cluster_num['1'], "States1" : cluster_states['1'] , "Cluster category1" : cluster_cat['1'],
     "Cluster name2": cluster_num['2'], "States2" : cluster_states['2'] , "Cluster category2" : cluster_cat['2'],
     "Cluster name3": cluster_num['3'], "States3" : cluster_states['3'] , "Cluster category3" : cluster_cat['3'],
     "Cluster name4": cluster_num['4'], "States4" : cluster_states['4'] , "Cluster category4" : cluster_cat['4'],
     
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


db.collection("Current cluster").document("Current").set(data)
db.collection("Current cluster").document("Current").update({u'data':True})