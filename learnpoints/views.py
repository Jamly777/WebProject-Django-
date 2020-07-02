from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from django.db.models import Sum
from . import models
import json
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# Create your views here.

def learnpoints(request):
    return render(request,'points.html')

def getpoints(request):
    code = {}
    code['Code']=''
    all_records=models.points.objects.all()
    points_dict=models.points.objects.aggregate(allpoints=Sum('points'))
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
                mail(food)
                points = 10 * float(times) + 5
                models.points.objects.create(date=date, learntime=times, points=points,
                                             allpoints=points_dict['allpoints'] + points)
    return HttpResponse(json.dumps(code))

def mail(text):
    from_addr='1368481098@qq.com'
    to_addr='849336620@qq.com'
    password='ouwwlemoszmkfiff'
    smtp_server='smtp.qq.com'
    msg=MIMEText(text)
    msg['From']=_format_addr('小阿黄呀小阿黄 <%s>' % from_addr)
    msg['To']=_format_addr('小阿号 <%s>' % to_addr)
    msg['Subject']=Header('小阿黄的食物分享','utf-8').encode()

    server=smtplib.SMTP_SSL(smtp_server,465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))