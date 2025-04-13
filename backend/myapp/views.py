
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.urls import reverse_lazy
from django.db.models import Avg, Max, Min, Sum
# Create your views here.
# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .forms import *

# Create your views here.
class HRDashboard(View):
    def get(self, request):
        context = {}
        return render(request, 'HR/HRDashboard.html', context)

    def post(self, request):
        pass

class DeptSetup(View):
    def get(self, request):
        dept = Department.objects.all()
        context = {'dept':dept}
        return render(request, 'HR/deptsetup.html', context)

    def post(self, request):
        detp = request.POST.get('detp')
        Department.objects.create(name=detp)
        # messages.success(request, 'Department Created Successfully')
        return JsonResponse({'status':'success', 'messages':'Department Created Successfully'})


class EmpSetup(View):
    def get(self, request):
        emp = Employee.objects.all()
        dept = Department.objects.all()
        fm = EmployeeForm()
        context = {'dept':dept, 'emp':emp, 'fm':fm}
        return render(request, 'HR/EmpSetup.html', context)

    def post(self, request):
        fm = EmployeeForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
        return redirect('EmpSetup')



