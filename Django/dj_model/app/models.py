from django.db import models

# Create your models here.
from django.core.validators import RegexValidator

class employee_table(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    emp_mail=models.EmailField()
    check_mobile=RegexValidator(regex="[6-9][0-9]{9}",message="enter 10 digits valid mobile number")
    emp_mobile=models.CharField(max_length=10,validators=[check_mobile])
    emp_joindate=models.DateField()
    emp_salary=models.FloatField()
    emp_image=models.ImageField(upload_to="images/",null=True,blank=True)
    emp_doc=models.FileField(upload_to="files/",null=True,blank=True)
    select_dep=[("hr","hr"),("sales","sales"),("it","it"),("admin","admin")]

    emp_dep=models.CharField(max_length=30,choices=select_dep)
