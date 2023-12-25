from django.db import models

# Create your models here.

class emp(models.Model):
    staffid=models.IntegerField()
    t_name=models.CharField(max_length=10,default="")
    w_name=models.CharField(max_length=10,default="")
    pda=models.CharField(max_length=10,default="")