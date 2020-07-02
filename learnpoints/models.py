from django.db import models
from rewords.models import points
# Create your models here.
class realtime(models.Model):
    date=models.CharField(max_length=255,primary_key=True)
    city=models.CharField(max_length=255)
    windspeed=models.CharField(max_length=255)
    direct=models.CharField(max_length=255)
    power=models.CharField(max_length=255)
    humidity=models.CharField(max_length=255)
    img=models.CharField(max_length=255)
    info=models.CharField(max_length=255)
    temperature=models.CharField(max_length=255)

class life(models.Model):
    date=models.CharField(max_length=255,primary_key=True)
    kongtiao=models.CharField(max_length=255)
    yundong=models.CharField(max_length=255)
    ziwaixian=models.CharField(max_length=255)
    ganmao=models.CharField(max_length=255)
    chuanyi=models.CharField(max_length=255)