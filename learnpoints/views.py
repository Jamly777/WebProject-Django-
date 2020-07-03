from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from . import models
import json
from django.core.mail import send_mail

# Create your views here.

def learnpoints(request):
    return render(request,'points.html')

def getpoints(request):
    code = {}
    code['Code']=''
    all_records=models.ponits_detail.objects.all()
    if request.method == 'GET':
        date=request.GET.get('date')
        #missme=on or None
        missme=request.GET.get('check')
        food=request.GET.get('food')
        times=request.GET.get('hours')
        if date == "":
            code['Code']='date_fail'
        elif missme == "dismiss":
            code['Code']='miss_fail'
        elif food == "":
            code['Code']='food_fail'
        elif times == "":
            code['Code']='times_fail'
        else:
            for i in range(len(all_records)):
                if date == all_records[i].date:
                    code['Code']='repeat_fail'
            if code['Code'] != 'repeat_fail':
                code['Code'] = 'SUCCESS'
                send_mail('食物分享',food,'',['849336620@qq.com'], fail_silently=False)
                points = 10 * float(times) + 5
                models.ponits_detail.objects.create(date=date, learntime=times, points=points)
                allpoints=models.ponits_detail.objects.get(id='0')
                allpoints += points
                allpoints.save()
    return HttpResponse(json.dumps(code))
