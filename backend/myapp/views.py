
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


#Shift Setup
class ShiftGroupSetup(View):
    # def get(self, request):
    #     shift_group = ShiftGroup.objects.all()
    #     context = {'shift_group':shift_group}
    #     return render(request, 'HR/ShiftGroupSetup.html', context)

    def post(self, request):
        shift_group = request.POST.get('groupName')
        working_hours = request.POST.get('workingHours')
        # print(shift_group, working_hours)
        ShiftGroup.objects.create(name=shift_group, working_hours=working_hours)
        # messages.success(request, 'Shift Group Created Successfully')
        return JsonResponse({'status':'success', 'messages':'Shift Group Created Successfully'})


class ShiftSetup(View):
    def get(self, request):
        shift = Shift.objects.all()
        shift_group = ShiftGroup.objects.all()
        fm = ShiftForm()
        context = {'sh':shift, 'shift_group':shift_group, 'fm':fm}
        return render(request, 'HR/ShiftSetup.html', context)

    def post(self, request):

        fm = ShiftForm(request.POST)
        if fm.is_valid():
            fm.save()
            print('save....')
            return JsonResponse({'status':'success', 'messages':'Shift Created Successfully'})
        else:
            print('not save....')
            return JsonResponse({'status':'error', 'messages':'Shift Creation Failed'})


#Sewing Line
class SewingLineSetup(View):
    def get(self, request):
        line = SewingLine.objects.all()
        fm = SewingLineForm()
        context={'line':line, 'fm':fm}
        return render(request, 'Sewing/SewingLineSetup.html', context)

    def post(self, request):
        fm = SewingLineForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('SewingLineSetup')

class SewingLineStatus(View):
    def post(self, request):
        sewing_line = request.POST.get('lid')
        sewing_line_obj = SewingLine.objects.get(id=sewing_line)
        sewing_line_obj.active = not sewing_line_obj.active
        sewing_line_obj.save()
        return JsonResponse({'status': 'success', 'messages': 'Sewing Line Status Updated Successfully'})

class LineTargetUpdate(View):
    def post(self, request):
        sewing_line = request.POST.get('lid')
        target = request.POST.get('target')
        sewing_line_obj = SewingLine.objects.get(id=sewing_line)
        sewing_line_obj.target = target
        sewing_line_obj.save()
        return JsonResponse({'status': 'success', 'messages': 'Sewing Line Target Updated Successfully'})
    


class EmployeeSewingLineSetup(View):
    def get(self, request,id):
        # emp = Employee.objects.all()
        sewing = SewingLine.objects.get(id=id)
        emp = Employee.objects.filter(sewing_line=sewing)
        line = SewingLine.objects.all()
        
        context = {'emp':emp, 'line':line}
        return render(request, 'Sewing/EmployeeSewingLineSetup.html', context)
