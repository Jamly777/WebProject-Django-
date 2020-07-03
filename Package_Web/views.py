from django.http import HttpRequest
import datetime
from learnpoints import models
from django.shortcuts import render

def mainpage(request):
    return render(request,'mainpage.html')


def index(request):
    date=str(datetime.datetime.now()).split()[0]
    data=models.life.objects.get(date=date)
    info=data.kongtiao+data.yundong+data.ziwaixian\
         +data.ganmao+data.chuanyi
    weather=models.realtime.objects.get(date=date)
    temp=weather.temperature
    city=weather.city
    tips=weather.info
    return render(request,'index.html',{'info':info,'city':city,
                                        'tips':tips,'temp':temp})
