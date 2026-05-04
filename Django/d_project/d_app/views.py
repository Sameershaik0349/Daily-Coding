from django.shortcuts import render

# http respose ==> it create new webpage and display our content

from django.http import HttpResponse

def first(reqest):
    return HttpResponse("<h1 style='color:green'>my django code</h1>")


def even(reqest):
    l=[]
    for i in range(10,20):
        if i%2==0:
            l.append(i)
    return HttpResponse(l)
