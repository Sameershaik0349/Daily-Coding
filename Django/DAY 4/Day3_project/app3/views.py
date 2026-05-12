from django.shortcuts import render

# Create your views here.


from app3.models import Employee_Table


def frotend(request):
    data = Employee_Table.objects.all()

    return render(request, "Html/front.html", {"data": data})