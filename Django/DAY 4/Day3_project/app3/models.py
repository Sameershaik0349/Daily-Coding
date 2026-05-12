from django.db import models

# Create your models here.



class Employee_Table(models.Model):
    emp_id=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=20)
    emp_sal=models.FloatField()
    dep=[('hr','hr'),('it','it'),("sales","sales"),("admin","admin")]
    emp_dep=models.CharField(max_length=30,choices=dep)
    emp_mail=models.EmailField(unique=True)



