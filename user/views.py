from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import video_form
from user.models import video
# Create your views here.
def home(request):
    return render(request,'index.html')

def admin(request):
    if request.method=='POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        if name == 'admin' and password == '14032001':
            return render(request,'admin.html')
    return render(request,"unsuccessful.html")


def submission(request):
    if request.method == "POST":
        form = video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"successful.html")
    return render(request,"unsuccessful.html")

def se(request):
    objects = video.objects.all()
    filtered = []
    for i in objects:
        arr = str(i).split()
        if arr[-1] == 'se':
            print(arr)
            filtered.append(i)
    return render(request,"se.html",{"all":filtered})

def daa(request):
    objects = video.objects.all()
    filtered = []
    for i in objects:
        arr = str(i).split()
        if arr[-1] == 'daa':
            print(arr)
            filtered.append(i)
    return render(request,"daa.html",{"all":filtered})

def cn(request):
    objects = video.objects.all()
    filtered = []
    for i in objects:
        arr = str(i).split()
        if arr[-1] == 'cn':
            print(arr)
            filtered.append(i)
    return render(request,"cn.html",{"all":filtered})


def ml(request):
    objects = video.objects.all()
    filtered = []
    for i in objects:
        arr = str(i).split()
        if arr[-1] == 'ml':
            print(arr)
            filtered.append(i)
    return render(request,"ml.html",{"all":filtered})

def admin_login(request):
    return render(request,'admin_login.html') 