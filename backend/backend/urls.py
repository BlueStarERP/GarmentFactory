"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('DeptSetup/', DeptSetup.as_view(), name='DeptSetup'),
    path('HRDashboard/', HRDashboard.as_view(), name='HRDashboard'),
    path('EmpSetup/', EmpSetup.as_view(), name='EmpSetup'),
    path('ShiftSetup/', ShiftSetup.as_view(), name='ShiftSetup'),
    path('ShiftGroupSetup/', ShiftGroupSetup.as_view(), name='ShiftGroupSetup'),
    path('SewingLineSetup/', SewingLineSetup.as_view(), name='SewingLineSetup'),
    path('SewingLineStatus/', SewingLineStatus.as_view(), name='SewingLineStatus'),
    path('LineTargetUpdate/', LineTargetUpdate.as_view(), name='LineTargetUpdate'),
    path('EmployeeSewingLineSetup/<int:id>/', EmployeeSewingLineSetup.as_view(), name='EmployeeSewingLineSetup'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)