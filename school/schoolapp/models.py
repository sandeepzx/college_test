from django.db import models

# Create your models here.
class Datas(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    materials = models.CharField(max_length=1000)


