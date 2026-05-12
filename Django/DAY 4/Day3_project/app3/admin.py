from django.contrib import admin

# Register your models here.

from app3.models import Employee_Table

class employee_admin(admin.ModelAdmin):
    list_display=["emp_id","emp_name","emp_dep","emp_sal","emp_mail"]


    ordering=["emp_id"]
    list_editable=["emp_mail","emp_name"]
    list_filter=["emp_dep"]
admin.site.register(Employee_Table,employee_admin)

    