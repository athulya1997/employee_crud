from django.db import models

# Create your models here.
class Reg1(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField	(max_length=50)
    mob=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Emp1(models.Model):
    emp_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.TextField()
    city=models.TextField()
    department=models.CharField(max_length=50)
    salary=models.FloatField()
    
    uid=models.ForeignKey(to=Reg1,on_delete=models.CASCADE)

