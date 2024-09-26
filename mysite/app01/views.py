from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Welcome")

def user_list(request):
    return HttpResponse("Userlist")

def user_add(request):
    return HttpResponse("UserAdd")