from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Datas

# Create your views here.
def home(req):
    return render(req, 'index.html')
def login(req):
    if req.method == 'POST':
        username = req.POST['username'] 
        password = req.POST['password'] 
        print(username)
        user = auth.authenticate(username=username,password= password)

        if user is not None:
            auth.login(req,user)
            return render(req, 'new.html')
        else:
            messages.info(req,"invalid Credentials")
    return render(req, 'login.html')

def logout(req):
    auth.logout(req)
    return render(req, 'index.html')
def Register(req):
    if req.method == 'POST':
        username = req.POST['username'] 
        password = req.POST['password'] 
        cpassword = req.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(req,"Username already taken")
                return render(req, 'register.html')
            else:
                user = User.objects.create_user(username = username,password=password)
                user.save()
                print("saved")
                
                return render(req, 'login.html')
        else:
            messages.info(req,"password not matching")
    
        
    return render(req, 'register.html')
    
def new(req):
    if req.method == 'POST':
        name = req.POST['name']
        dob = req.POST['dob']
        age = req.POST['age']
        gender = req.POST['gender']
        phone = req.POST['phone']
        mail = req.POST['mail']
        department = req.POST['department']
        course = req.POST['course']
        purpose = req.POST['purpose']
        materials =[]
        if 'material1' in req.POST:
            materials.append('Note Book')
        if 'material2' in req.POST:
            materials.append('Pen')
        if 'material3' in req.POST:
            materials.append('Exam Papers')
        
        data = Datas.objects.create(name=name,dob=dob,age=age,gender=gender,phone=phone,email=mail,department=department,course=course,purpose=purpose,materials=materials)
        data.save()
        print("saved")
        messages.info(req,"Order Confirmed")
        return render(req, 'new.html')
    else:
        messages.info(req,"invalid Credentials")
        return render(req, 'new.html')
    return render(req, 'new.html')

def n(req):
    return render(req,"ind.html")
