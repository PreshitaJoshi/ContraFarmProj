from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import *

from django.views.decorators.csrf import csrf_exempt
#from app.forms import *
import json
from urllib.parse import urlparse, parse_qs

from rest_framework import parsers
from json import JSONDecodeError
from django.http import JsonResponse
from random import*
import base64
import io
from PIL import Image
from django.core.files.base import ContentFile
import PIL.Image as Image
from django.core.files import File
import pyrebase

# Create your views here.

#Firebase Data
config={
  "apiKey": "AIzaSyBzvM3fXYdUeN9MzsAuGF8Btscg9Lg6LDE",
  "authDomain": "hydroponic-project-78a27.firebaseapp.com",
  "databaseURL":"https://hydroponic-project-78a27-default-rtdb.firebaseio.com",
  "projectId": "hydroponic-project-78a27",
  "storageBucket": "hydroponic-project-78a27.appspot.com",
  "messagingSenderId": "857344418366",
  "appId": "1:857344418366:web:204c27366e3cdf6e69e76f",
  "measurementId": "G-2X2707CKT5"
}

firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()




@csrf_exempt
def datafromsensor():
    conductivity=database.child('Hydroponic').child('Conductivity').get().val()
    phsensor=database.child('Hydroponic').child('Phsensor').get().val()
    maintank=database.child('Hydroponic').child('MainTank').get().val()
    tank1=database.child('Hydroponic').child('Tank1').get().val()
    tank2=database.child('Hydroponic').child('Tank2').get().val()
    tank3=database.child('Hydroponic').child('Tank3').get().val()
    tank4=database.child('Hydroponic').child('Tank4').get().val()
    temp=database.child('Hydroponic').child('Temp').get().val()
    
    
    print("*************Data From Firebase *******************")
    newdata=FirebaseData(Conductivity=conductivity,Phsensor=phsensor,MainTank=maintank,Tank1=tank1,Tank2=tank2,Tank3=tank3,Tank4=tank4,Temp=temp)
    newdata.save()

@csrf_exempt
def tankdata(request):
    maintank=database.child('Hydroponic').child('MainTank').get().val()
    tank1=database.child('Hydroponic').child('Tank1').get().val()
    tank2=database.child('Hydroponic').child('Tank2').get().val()
    tank3=database.child('Hydroponic').child('Tank3').get().val()
    tank4=database.child('Hydroponic').child('Tank4').get().val()

                
    
    result_prev={
        'Main Tank':maintank,
        'Tank1':tank1,
        'Tank2':tank2,
        'Tank3':tank3,
        'Tank4':tank4
    }

    result={
                    "responseCode":200,
                    "responseMessage":"",
                    "responseData":result_prev
                    }
    

    return JsonResponse(result)


@csrf_exempt
def temperaturedata(request):
    temp=database.child('Hydroponic').child('Temp').get().val()
    result_prev={
        'Temperature':temp
    }
    result={
                    "responseCode":200,
                    "responseMessage":"",
                    "responseData":result_prev
                    }
    

    return JsonResponse(result)

@csrf_exempt
def ph_tdsdata(request):
    conductivity=database.child('Hydroponic').child('Conductivity').get().val()
    phsensor=database.child('Hydroponic').child('Phsensor').get().val()
    result_prev={
        'Conductivity':conductivity,
        'Phsensor':phsensor
    }
    result={
                    "responseCode":200,
                    "responseMessage":"",
                    "responseData":result_prev
                    }
    

    return JsonResponse(result)

@csrf_exempt
def all_weekly_data(request):
    resultdic={}
    resultlist=[]
    udata={}
       
    import datetime
    from datetime import date, timedelta
    
    today1 =datetime.datetime.now()

    last_week = today1 - datetime.timedelta(days=7)

    alldata=FirebaseData.objects.filter(is_created__range=[last_week, today1])

    if alldata:
        for j in alldata:
                        udata={
                            'Date':j.is_created,
                            'Ph Data':j.Phsensor,
                            'Temperature':j.Temp,
                            'EC Data':j.Conductivity,
                            'Main Tank':j.MainTank,
                            'Tank 1':j.Tank1,
                            'Tank 2':j.Tank2,
                            'Tank 3':j.Tank3,
                            'Tank 4':j.Tank4,


                        }
                        
                        resultlist.append(udata)
        resultdic["Result"]=resultlist
        print(resultdic)
        result={
                    "responseCode":200,
                    "responseMessage":"",
                    "responseData":resultdic
                    }
    
        return JsonResponse(result)
    else:
        result={
                    "responseCode":500,
                    "responseMessage":"Weekly Data Can Not Fetch",
                    "responseData":""
                    }
        return JsonResponse(result)


'''@csrf_exempt
def temperature_weekdata(request):
    resultdic={}
    resultlist=[]
    udata={}
       
    import datetime
    from datetime import date, timedelta
    
    today1 =datetime.datetime.now()

    last_week = today1 - datetime.timedelta(days=7)

    alldata=FirebaseData.objects.filter(is_created__range=[last_week, today1])

    if alldata:

        for j in alldata:
                        udata={
                            'Date':j.is_created,
                            


                        }
                        
                        resultlist.append(udata)
        resultdic["Result"]=resultlist
        print(resultdic)
        result={
                    "responseCode":200,
                    "responseMessage":"",
                    "responseData":resultdic
                    
                    }
    
        return JsonResponse(result)
    else:
        result={
                    "responseCode":500,
                    "responseMessage":"Weekly Data Can Not Fetch",
                    "responseData":""
                    
                    }
        return JsonResponse(result)

'''

'''@csrf_exempt
def maintank_waterlevel_weekdata(request):
    resultdic={}
    resultlist=[]
    udata={}
       
    import datetime
    from datetime import date, timedelta
    
    today1 =datetime.datetime.now()

    last_week = today1 - datetime.timedelta(days=7)

    alldata=FirebaseData.objects.filter(is_created__range=[last_week, today1])

    if alldata:

        for j in alldata:
                        udata={
                            'Date':j.is_created,
                            'MainTank_water_level':j.MainTank


                        }
                        
                        resultlist.append(udata)
        resultdic["Result"]=resultlist
        print(resultdic)
        result={
                    "responseCode":200,
                    "responseMessage":"",
                    "responseData":resultdic
                    
                    }
    
        return JsonResponse(result)
    else:
        result={
                    "responseCode":500,
                    "responseMessage":"Weekly Data Can Not Fetch",
                    "responseData":""
                  
                    }
        return JsonResponse(result)
'''

'''@csrf_exempt
def ec_weekdata(request):
    resultdic={}
    resultlist=[]
    udata={}
       
    import datetime
    from datetime import date, timedelta
    
    today1 =datetime.datetime.now()

    last_week = today1 - datetime.timedelta(days=7)

    alldata=FirebaseData.objects.filter(is_created__range=[last_week, today1])

    if alldata:

        for j in alldata:
                        udata={
                            'Date':j.is_created,
                            


                        }
                        
                        resultlist.append(udata)
        resultdic["Result"]=resultlist
        print(resultdic)
        result={
                    "responseCode":200,
                    "responseMessage":"",
                    "responseData":resultdic
                    
                    }
    
        return JsonResponse(result)

    else:
        result={
                    "responseCode":500,
                    "responseMessage":"Weekly Data Can Not Fetch",
                    "responseData":""
                    
                    }
        return JsonResponse(result)



'''


@csrf_exempt
def lights_data(request):
    top=request.POST["top"]
    #top = request.POST.get("top", "Guest")
    left=request.POST['left']
    right=request.POST['right']
    intensity=request.POST['intensity']
    start_time=request.POST['start_time']
    end_time=request.POST['end_time']

    
    print("Data Get Successfuly************")

    database.child('Hydroponic').child('LeftLight').set(left)
    database.child('Hydroponic').child('RightLight').set(right)
    database.child('Hydroponic').child('TopLight').set(top)
    database.child('Hydroponic').child('IntensityOfLight').set(intensity)

    print("*********** Data Save Success*************")
    #return JsonResponse("All Data Deleted Successfuly")
    result={
                    "responseCode":200,
                    "responseMessage":"Data Save Successfuly",
                    "responseData":""
                    
                    }
    return JsonResponse(result)

@csrf_exempt
def delete_alldata(request):
    FirebaseData.objects.all().delete()
    print("Data Deleted")
    result={
                    "responseCode":500,
                    "responseMessage":"All Data Deleted Successfuly",
                    "responseData":""
                    
                    }
    return JsonResponse(result)
    
    