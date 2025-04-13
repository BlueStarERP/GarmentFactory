from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['department', 'employee_id','employee_name','position','gender','date_of_birth','ssb_id','nrc_no','fathername','mothername','hire_date','salary','phone','address','photo','familytable','nrc_photo']
        exclude = ['user', 'created_at']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control col-sm-6 col-md-4'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control col-sm-6 col-md-4'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control col-sm-6 col-md-4', 'accept': 'image/*'}),
            'familytable': forms.ClearableFileInput(attrs={'class': 'form-control col-sm-6 col-md-4', 'accept': 'image/*'}),
            'nrc_photo': forms.ClearableFileInput(attrs={'class': 'form-control col-sm-6 col-md-4', 'accept': 'image/*'}),
            'department': forms.Select(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'employee_name': forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'position': forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'gender': forms.Select(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'ssb_id': forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'nrc_no': forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'fathername': forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'mothername': forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'phone': forms.TextInput(attrs={'class': 'form-control col-sm-12 col-md-4'}),
            'address': forms.Textarea(attrs={'class': 'form-control col-sm-12 col-md-4', 'rows': 3}),


        }