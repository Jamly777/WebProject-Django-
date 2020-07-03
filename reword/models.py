from django.db import models
# Create your models here.

class ponits_detail(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.CharField(max_length=20)
    learntime=models.DecimalField(decimal_places=1,max_digits=6)
    points=models.IntegerField()
    info=models.CharField(max_length=100)

class learnpoints(models.Model):
    id=models.IntegerField(primary_key=True)
    points=models.IntegerField()