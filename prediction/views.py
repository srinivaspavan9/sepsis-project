from django.shortcuts import render
import pandas as pd
import pickle
from sklearn.externals import joblib
import pickle
from sklearn.preprocessing import MinMaxScaler
def graphs(request):
    return render(request,'prediction/graphs.html')

def formhandle(request):
    if(request.method=='POST'):
        gen=request.POST['gender']
        hr=request.POST['heartrate']
        temp=request.POST['temp']
        age = request.POST['age']
        oxy =request.POST['oxygen']
        bp = request.POST['bp']
        resp = request.POST['resp']
        iculos = request.POST['iculos']
        time = request.POST['time']
        gen=int(gen)
        hr=int(hr)
        temp=int(temp)
        age=int(age)
        oxy=int(oxy)
        resp=int(resp)
        iculos=int(iculos)
        print(gen)
        print(hr)
        print(temp)
        print(age)
        print(oxy)
        print(bp)
        print(resp)
        print(iculos)
        #New code starts from here
        if(hr>=100 and age>=10):
            hr='abnormal'
        elif(hr<100 and hr>60 and age>=10):
            hr='normal'
        elif(hr>=70 and hr<190 and age<10):
            hr='normal'
        elif(hr<70 and hr>=190 and age<10):
            hr='abnormal'
        else:
            hr='Missing'

        if(temp>=36.4 and temp<37.6):
            temp='normal'
        elif(temp<36.4 and temp>=37.6):
            temp='abnormal'
        else:
            temp='Missing'

        if (resp >=30 and resp <=60 and age<1):
            resp='normal'
        elif((resp<30 or resp>60 ) and age<1):
            resp='abnormal'
        elif(resp>=24 and resp<=40 and age>=1 and age<=3):
            resp='normal'
        elif((resp<24 or resp>40) and age>=1 and age<=3):
            resp='abnormal'
        elif(resp>=22 and resp<=34 and age>=3 and age<=6):
            resp='normal'
        elif((resp<22 or resp>34) and age>=3 and age<=6):
            resp='abnormal'
        elif((resp>=18 and resp<=30) and age<=6 and age>=12):
            resp='normal'
        elif((resp<18 or resp>30) and age>=6 and age<=12):
            resp='abnormal'
        elif((resp >=12 and resp <=20) and age>12):
            resp='normal'
        elif((resp<12 or resp>20) and age>12):
            resp='abnormal'
        else:
            resp='Missing'

        if(age>65):
            age='old'
        elif(age<1):
            age='infant'
        else:
            age='child/adult'

        if(oxy>=90 and oxy<100):
            oxy='normal'
        elif(oxy<90 and oxy>=0):
            oxy='abnormal'
        else:
            oxy='Missing'
        #New code ends here
        mymodel=joblib.load('C:\\Users\\srinivas pavan\\PycharmProjects\\Prediction\\seppred\\sepsis\\log_model2.pkl')
        mydf = pd.DataFrame({'Gender': int(gen), 'custom_hr': hr, 'custom_temp': temp, 'custom_age': age,
                             'custom_o2stat': oxy, 'custom_bp': bp, 'custom_resp': resp, 'ICULOS': int(iculos),
                             'HospAdmTime': -2.45}, index=[0])
        print(mydf)
        val=mymodel.predict(mydf)
        if val==[0] :
            val=0
        else:
            val=1

        print('myvalue :'+str(val))
        return render(request,'prediction/prediction.html',{'val':val})
    else:
        return render(request,'prediction/prediction.html')
