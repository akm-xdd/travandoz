from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login(request):
     
     return render(request,'authentication/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        c_password = request.POST['password2']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = name

        myuser.save() 
        messages.success(request,"Your Account has been created")

        return redirect('signin')  


    return render(request,'authentication/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request)
            fname = user.first_name
            #messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return render(request,'authentication/index.html')
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    return redirect('login')
    
