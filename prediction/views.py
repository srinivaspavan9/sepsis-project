from django.shortcuts import render
import pandas as pd
import pickle
from sklearn.externals import joblib
import pickle
from sklearn.preprocessing import MinMaxScaler


def formhandle(request):
    if(request.method=='POST'):
        gen=request.POST['gender']
        hr=request.POST['heartrate']
        temp= request.POST['temp']
        age = request.POST['age']
        oxy = request.POST['oxygen']
        bp = request.POST['bp']
        resp = request.POST['resp']
        iculos = request.POST['iculos']
        time = request.POST['time']
        mymodel=joblib.load('C:\\Users\\srinivas pavan\\PycharmProjects\\Prediction\\seppred\\sepsis\\log_model.pkl')
        mydf = pd.DataFrame({'Gender': int(gen), 'custom_hr': hr, 'custom_temp': temp, 'custom_age': age,
                             'custom_o2stat': oxy, 'custom_bp': bp, 'custom_resp': resp, 'ICULOS': int(iculos),
                             'HospAdmTime': -2.45}, index=[0])
        print(mydf)
        val=mymodel.predict(mydf)
        if val==[0]:
            val='No chance of sepsis'
        else:
            val='Chances of sepsis are high'
        print('myvalue :'+str(val))
        return render(request,'prediction/prediction.html',{'val':val})
    else:
        return render(request,'prediction/prediction.html')

