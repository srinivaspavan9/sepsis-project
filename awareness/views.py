from django.shortcuts import render

def home(request):
    return render(request,'awareness/index.html')

def base(request):
    return render(request,'awareness/base.html')