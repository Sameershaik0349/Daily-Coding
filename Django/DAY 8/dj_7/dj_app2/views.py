from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def app2fun1(request):
    return HttpResponse("<h1>app2 fun 1<h1>")
def app2fun2(request):
    return HttpResponse("<h1>app2 fun 2<h1>")
def app2fun3(request):
    return HttpResponse("<h1>app2 fun 3<h1>")
