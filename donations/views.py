from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user

# Create your views here.
def home(req):
    return render(req,"donations/index.html")

def signup(req):
    if req.method=="POST":
        name=req.POST['name']
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        district=req.POST['district']
        data=Volunteer(name2=name,username2=username,email2=email,password2=password,district2=district)
        data.save()
        messages.success(req,"your data added successfully")
        messages.info(req,"check your mail or password")
        return render(req,"donations/login.html")
    return render(req,"donations/signup.html")

def login(req):
    if req.method=="POST":
        username=req.POST['username']
        emaill=req.POST['email']
        pswd=req.POST['password']

        try:
            data=Volunteer.objects.get(username2=username)
            if(data.password2==pswd and data.email2==emaill):
                return render(req,"donations/index3.html")
            return HttpResponse("INVALID PASSWORD")
        except:
            return HttpResponse("USERNAME IS NOT FOUND")
    return render(req,"donations/login.html")

def signup1(req):
    if req.method=="POST":
        name=req.POST['name']
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        district=req.POST['district']
        data=NGO(name=name,username=username,email=email,password=password,district=district)
        data.save()
        messages.success(req,"your data added successfully")
        messages.info(req,"check your mail or password")
        return render(req,"donations/login1.html")
    return render(req,"donations/signup1.html")

def login1(req):
    if req.method=="POST":
        username=req.POST['username']
        emaill=req.POST['email']
        pswd=req.POST['password']

        try:
            data=NGO.objects.get(username=username)
            if(data.password==pswd and data.email==emaill):
                return render(req,"donations/index1.html")
            return HttpResponse("INVALID PASSWORD")
        except:
            return HttpResponse("USERNAME IS NOT FOUND")

    return render(req,"donations/login1.html")

def signup2(req):
    if req.method=="POST":
        name2=req.POST['name2']
        username2=req.POST['username2']
        email2=req.POST['email2']
        password2=req.POST['password2']
        district2=req.POST['district2']
        data=Public(name1=name2,username1=username2,email1=email2,password1=password2,district1=district2)
        data.save()
        messages.success(req,"your data added successfully")
        messages.info(req,"check your mail or password")
        return render(req,"donations/login2.html")
    return render(req,"donations/signup2.html")

def login2(req):
    if req.method=="POST":
        username2=req.POST['username2']
        emaill2=req.POST['email2']
        pswd2=req.POST['password2']

        try:
            data=Public.objects.get(username1=username2)
            if(data.password1==pswd2 and data.email1==emaill2):
                return render(req,"donations/index2.html")
            return HttpResponse("INVALID PASSWORD")
        except:
            return HttpResponse("USERNAME IS NOT FOUND")
    return render(req,"donations/login2.html")


def home1(req):
    return render(req,"donations/index1.html")


def home2(req):
    return render(req,"donations/index2.html")

def home3(req):
    return render(req,"donations/index3.html")


def event(req):
    if req.method=="POST":
        name4=req.POST['name']
        mobile4=req.POST['mobile']
        address4=req.POST['address']
        date4=req.POST['date']
        time4=req.POST['time']

        data=Event(name4=name4,mobile4=mobile4,address4=address4,date4=date4,time4=time4)
        data.save()
        messages.success(req,"your data added successfully")
        messages.info(req,"check your mail or password")
        return render(req,"donations/index2.html")
    return render(req,"donations/event.html")

def gathering(req):
    if req.method=="POST":
        name5=req.POST['name']
        place5=req.POST['place']
        cause5=req.POST['cause']
        date5=req.POST['date']
        time5=req.POST['time']

        data=Gathering(name5=name5,place5=place5,cause5=cause5,date5=date5,time5=time5)
        data.save()
        messages.success(req,"your data added successfully")
        messages.info(req,"check your mail or password")
        return render(req,"donations/index1.html")
    return render(req,"donations/gathering.html")



def logout1(req):
    logout(req)
    return redirect('/')

def event1(req):
    eventclass = Event()
    p= eventclass.get_values()
    p1= eventclass.get_length()
    return render(req,"donations/event1.html",{"p":p,"p1":p1})

def upcoming(req):
    eventclass1 = Gathering()
    q= eventclass1.get_values1()
    q1= eventclass1.get_length1()
    return render(req,"donations/upcoming.html",{"q":q,"q1":q1})

