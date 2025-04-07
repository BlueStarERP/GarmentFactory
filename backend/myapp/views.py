
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

# Create your views here.
