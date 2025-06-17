from django.db import models
class Vehicle(models.Model):
    Vehicle_Name=models.CharField()
    Brand=models.CharField()
    Color=models.CharField()
    Milage=models.IntegerField()
    Image=models.ImageField(upload_to='v')