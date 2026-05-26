from django.urls import path
from dj_app2.views import app2fun1,app2fun2,app2fun3


urlpatterns = [
    path('',app2fun1,name="app2"),
    path('app2f2/',app2fun2),
    path('app2f3/',app2fun3),
]