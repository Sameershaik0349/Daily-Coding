from django.urls import path
from dj_app.views import fun1,fun2,fun3


urlpatterns = [
    path('',fun1),
    path('f2/',fun2),
    path('f3/',fun3),
]