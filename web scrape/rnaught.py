# ------@gROUP 18---------------#
from bs4 import BeautifulSoup
import requests
import numpy as np

page1 = requests.get('http://covid-19.moh.gov.my/terkini').text
soup1 = BeautifulSoup(page1,'html.parser')      #Get page source
rnaught=soup1.findAll("div", {"id" : "custom-2550-particle"} , {"class": "g-content g-particle"})

rnaught=str(rnaught)

rDate = rnaught.split('/kajian-dan-penyelidikan/nilai-r-malaysia">',1)[1]   #Needing Respiratory Assistance Cases
rDate= rDate.split(' <strong><span style="',1)[0]

r0 = rnaught.split('rgb(184, 49, 47);">',1)[1]   #Needing Respiratory Assistance Cases
r0= r0.split('</span></strong></a>',1)[0]

