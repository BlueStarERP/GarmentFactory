from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class SewingLine(models.Model):
    name = models.CharField(max_length=100)
    target = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    employee_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    employee_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=[
        ('male', 'Male'),
        ('female', 'Female'),

    ])
    date_of_birth = models.DateField()
    ssb_id = models.CharField(max_length=225, blank=True, null=True)
    nrc_no = models.CharField(max_length=225, unique=True)
    fathername = models.CharField(max_length=225)
    mothername = models.CharField(max_length=225)

    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    sewing_line = models.ForeignKey(SewingLine, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='profile', blank=True, null=True)
    familytable = models.ImageField(upload_to='familytable', blank=True, null=True)
    nrc_photo = models.ImageField(upload_to='nrc', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('leave', 'On Leave'),
    ])
    
    def __str__(self):
        return f"{self.employee} - {self.date}"

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date}"
    

class ShiftGroup(models.Model):
    name = models.CharField(max_length=100)
    working_hours = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Shift(models.Model):
    shift_group = models.ForeignKey(ShiftGroup, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    working_hours = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.start_time} - {self.end_time}"
    



class SewingLineEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sewing_line = models.ForeignKey(SewingLine, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    srno = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.employee} - {self.sewing_line} - {self.shift}"

class EmployeeCMPReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sewing_line = models.ForeignKey(SewingLine, on_delete=models.CASCADE)
    date = models.DateField()
    shift_c = models.IntegerField(default=0)
    target = models.IntegerField(default=0)
    actual = models.IntegerField(default=0)
    
    shift1 = models.IntegerField(default=0)
    shift2 = models.IntegerField(default=0)
    shift3 = models.IntegerField(default=0)
    shift4 = models.IntegerField(default=0)
    shift5 = models.IntegerField(default=0)
    shift6 = models.IntegerField(default=0)
    shift7 = models.IntegerField(default=0)
    shift8 = models.IntegerField(default=0)
    shift9 = models.IntegerField(default=0)
    shift10 = models.IntegerField(default=0)
    shift11 = models.IntegerField(default=0)
    shift12 = models.IntegerField(default=0)
    shift13 = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.employee} - {self.sewing_line} - {self.date}"