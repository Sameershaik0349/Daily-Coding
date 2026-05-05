"""
URL configuration for d_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from d_app.views import even
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",first),
    # path("even/",even)
    # path("",employee)
    # path("",employee)
    # path("<int:val1>/<int:val2>/",cal)
    # path("<str:emp_name>/<int:emp_id>/<int:emp_sal>/",emp)
    path("<int:val>/",even)
]
