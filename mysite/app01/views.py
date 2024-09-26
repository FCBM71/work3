from django.shortcuts import render, HttpResponse
from .models import Profile

def home(request):
    profile= Profile(name='Runnan He', bio='To be done', email='mcx_lvr@sjtu.edu.cn')
    #profile = Profile.objects.first()  
    return render(request, 'app01/home.html', {'profile': profile})

def index(request):
    return HttpResponse("Welcome")

def user_list(request):
    return HttpResponse("Userlist")

def user_add(request):
    return HttpResponse("UserAdd")