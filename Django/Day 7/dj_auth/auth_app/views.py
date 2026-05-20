from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def emp_reg(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        p2 = request.POST.get('c_password')

        if password != p2:
            return HttpResponse("<h1>Password does not match</h1>")

        elif User.objects.filter(email=email).exists():
            return HttpResponse("<h1>User already exists</h1>")

        else:
            s = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            s.save()

            return HttpResponse("<h1>Registration successful</h1>")

    return render(request, 'Html/index.html')



def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("<h1> Login succesfull</h1>")
        else:
            return HttpResponse("<h1>invalid credentials</h1>")
    return render(request, 'Html/indexlog.html')
