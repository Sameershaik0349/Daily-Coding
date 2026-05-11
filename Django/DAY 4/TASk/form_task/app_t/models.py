from django.db import models

# Create your models here.


class employee_table(models.Model):
    emp_id=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=30)
    emp_dep=models.CharField(max_length=30)

