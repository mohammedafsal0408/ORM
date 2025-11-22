from django.db import models
from django.contrib import admin
class product(models.Model):
    productid=models.CharField(primary_key=True,max_length=8)
    productName=models.CharField(max_length=30)
    price=models.FloatField()
    rating=models.FloatField()
    Deldate=models.DateTimeField()
    company=models.CharField(max_length=20)
    stock=models.CharField(max_length=20)

class productAdmin(admin.ModelAdmin):
    list_display=["productid","productName","price","rating","Deldate","company","stock"]
