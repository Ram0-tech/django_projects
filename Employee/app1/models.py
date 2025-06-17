from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField()
    place=models.CharField()
    image=models.ImageField(upload_to='employee')
    department_name=models.CharField()
