from django.contrib import admin

# Register your models here.

from app.models import employee_table


class employee_admin(admin.ModelAdmin):
    list_display=["emp_id","emp_name","emp_mail","emp_salary","emp_joindate","emp_mobile","emp_image","emp_doc","emp_dep"]


admin.site.register(employee_table,employee_admin)