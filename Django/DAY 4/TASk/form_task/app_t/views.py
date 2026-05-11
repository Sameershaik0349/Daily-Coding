from django.shortcuts import render

# Create your views here.


from app_t.models import employee_table

def front(request):
    messege=""
    if request.method=="POST":
        emp_id=request.POST.get("emp_id")
        emp_name=request.POST.get("emp_name")
        emp_dep=request.POST.get("emp_dep")

        if emp_id=="" or emp_name=="" or emp_dep=="":
            messege ="fill all fields"
        else:

            employee_table.objects.create(
                emp_id=emp_id,
                emp_name=emp_name,
                emp_dep=emp_dep
            )
            messege = "Data Stored Successfully"


    data=employee_table.objects.all()
    return render(request,"Html/front.html",{"data":data,"messege":messege})
