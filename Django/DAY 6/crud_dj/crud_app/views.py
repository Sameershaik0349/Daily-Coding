from django.shortcuts import render

# Create your views here.
from crud_app.forms import emp_form

from crud_app.models import employee


def crud(request):
    data=employee.objects.all()
    form=emp_form()
    if request.method=='POST':
        form=emp_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect("crud")
    return render(request,'Day_6/app_tem.html',{"data":data,"form":form})