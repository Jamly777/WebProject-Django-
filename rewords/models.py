from django.db import models

# Create your models here.
class points(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True)
    date=models.CharField(max_length=20)
    learntime=models.DecimalField(max_digits=4,decimal_places=1)
    points=models.IntegerField(default=0)
    allpoints=models.IntegerField(default=0)

