from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from . import models
from django.core.mail import send_mail
import datetime
import json

# Create your views here.

def reword(request):
    allpoints = models.learnpoints.objects.get(id='0')
    return render(request,'reword.html',{'points':allpoints.points})

def getreword(request):
    code={}
    date=datetime.datetime.now()
    if request.method == 'POST':
        price=int(request.POST.get('price'))
        points=int(request.POST.get('point'))
        goodsname=request.POST.get('goods')
        print(price,points,goodsname)
        if price == 0 :
            code['Code']='FAIL'
            code['info']='选择奖品'
        elif points >= price:
            rest=points - price
            code['Code']='SUCCESS'
            code['learn']=rest
            models.ponits_detail.objects.create(date=str(date).split()[0],learntime=0,
                                                points=-rest,info='兑换奖品')
            ponints=models.learnpoints.objects.get(id='0')
            ponints.points=rest
            ponints.save()
            #send_mail('奖品的兑换','小小黄兑换了'+goodsname,'',['1368481098@qq.com'], fail_silently=False)
        else:
            code['Code']='FAIL'
            code['info']='学习点不够'
    return HttpResponse(json.dumps(code))