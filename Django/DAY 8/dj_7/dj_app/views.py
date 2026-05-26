from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def fun1(request):
    data='app1fun1'
    return render(request, 'HTML/app.html',{'msg':data})
def fun2(request):
    return HttpResponse("<h1>app1 fun 2<h1>")
def fun3(request):
    return HttpResponse("<h1>app1 fun 3<h1>")

