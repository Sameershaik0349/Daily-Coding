from django.shortcuts import render, redirect
from crud_app.forms import emp_form
from crud_app.models import employee

def crud(request):
    data = employee.objects.all()
    form = emp_form()

    if request.method == 'POST':
        form = emp_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect("crud")

    return render(request, 'Day_6/app_tem.html', {
        "data": data,
        "form": form
    })

def up_del(request, id):
    data = employee.objects.get(id=id)

    form = emp_form(instance=data)

    if request.method == 'POST':
        form = emp_form(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return redirect("crud")
        
    return render(request, 'Day_6/app1_tem.html', {

        "data": data,
        "form": form
    })



def delete(request, id):
    data = employee.objects.get(id=id)
    data.delete()
    return redirect("crud")


