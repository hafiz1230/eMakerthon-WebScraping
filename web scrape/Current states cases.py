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
    sep1= '\xa0'
    sep2= ' '
    td_cases = td_cases.split(sep, -1)[0]
    td_symbol=td_symbol.split(sep1, -1)[0]
    td_symbol=td_symbol.replace("WP KUALA LUMPUR", "KL")
    td_symbol=td_symbol.replace("WP PUTRAJAYA", "PUTRAJAYA")
    td_symbol=td_symbol.replace("WP LABUAN", "LABUAN")
    td_symbol=td_symbol.split(sep2, -1)[0]
    num_cases[td_symbol]=td_cases
    num_cases= num_cases

data = {
    "Article Date": date,    #Store "date" in dict
    "Selangor": int(num_cases['SELANGOR'].replace(',' , '')),     #Assigned int and remove " , "
    "Sabah": int(num_cases['SABAH'].replace(',' , '')),
    "Johor": int(num_cases['JOHOR'].replace(',' , '')),
    "WP Kuala Lumpur": int(num_cases['KL'].replace(',' , '')),
    "Negeri Sembilan": int(num_cases['NEGERI'].replace(',' , '')),
    "Sarawak": int(num_cases['SARAWAK'].replace(',' , '')),
    "Pulau Pinang": int(num_cases['PULAU'].replace(',' , '')),
    "Perak":  int(num_cases['PERAK'].replace(',' , '')),
    "Kedah": int(num_cases['KEDAH'].replace(',' , '')),
    "Melaka": int(num_cases['MELAKA'].replace(',' , '')),
    "Kelantan": int(num_cases['KELANTAN'].replace(',' , '')), 
    "Pahang": int(num_cases['PAHANG'].replace(',' , '')),
    "Terengganu": int(num_cases['TERENGGANU'].replace(',' , '')),
    "WP Labuan": int(num_cases['LABUAN'].replace(',' , '')),
    "WP Putrajaya": int(num_cases['PUTRAJAYA'].replace(',' , '')),
    "Perlis": int(num_cases['PERLIS'].replace(',' , '')),
    "Jumlah Keseluruhan": int(num_cases['JUMLAH'].replace(',' , '')),

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

db.collection("Current covid states cases").document("Current").set(data)
db.collection("Current covid states cases").document("Current").update({u'data':True})
