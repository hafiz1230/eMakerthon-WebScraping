
data1={   ## Store in json file

     "image" : "https://raw.githubusercontent.com/hafiz1230/finalforecasting/main/forecastpic/1.png",
     "title" : "Number of Covid-19 cases in Malaysia",
     
     
}

data2={

     "image" : "https://raw.githubusercontent.com/hafiz1230/finalforecasting/main/forecastpic/2.png",
     "title" : "Number of Covid-19 cases in Malaysia Group by Years",
     
}

data3={

     "image" : "https://raw.githubusercontent.com/hafiz1230/finalforecasting/main/forecastpic/3.png",
     "title" : "Number of Covid-19 cases in Malaysia Group by Months",
     
}

data4={

     "image" : "https://raw.githubusercontent.com/hafiz1230/finalforecasting/main/forecastpic/4.png",
     "title" :  "Number of Covid-19 cases in Malaysia group by 'Year', 'Month'",
     
}

data5={

     "image" : "https://raw.githubusercontent.com/hafiz1230/finalforecasting/main/forecastpic/5.png",
     "title" : "Daily Cases"
     
}

data6={

     "image" : "https://raw.githubusercontent.com/hafiz1230/finalforecasting/main/forecastpic/6.png",
     "title" : "Number of Covid-19 cases in Malaysia from December 2020 to March 2021",
     
}

data7={

     "image" : "https://raw.githubusercontent.com/hafiz1230/finalforecasting/main/forecastpic/7.png",
     "title" : "Prediction of the number of Covid-19 cases in Malaysia in March using Holt-Winter Forecast",
     
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

db.collection("Forecasting").document("1").set(data1)  ## Store in firestore
db.collection("Forecasting").document("1").update({u'data1':True})  ## Update in firestore

db.collection("Forecasting").document('2').set(data2)
db.collection("Forecasting").document('2').update({u'data2':True})

db.collection("Forecasting").document('3').set(data3)
db.collection("Forecasting").document('3').update({u'data3':True})

db.collection("Forecasting").document('4').set(data4)
db.collection("Forecasting").document('4').update({u'data4':True})

db.collection("Forecasting").document('5').set(data5)
db.collection("Forecasting").document('5').update({u'data5':True})

db.collection("Forecasting").document('6').set(data6)
db.collection("Forecasting").document('6').update({u'data6':True})

db.collection("Forecasting").document('7').set(data7)
db.collection("Forecasting").document('7').update({u'data7':True})
