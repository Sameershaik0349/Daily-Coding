from django.db import models

# Create your models here.


class employee(models.Model):
    emp_id=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=30,unique=True)
    emp_age=models.IntegerField()
    emp_email=models.EmailField(unique=True)