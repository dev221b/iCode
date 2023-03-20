from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'authentication/home.html')

def index(request):
    return render(request, 'authentication/index.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            name = user.first_name
            return render(request, 'authentication/index.html', {'name': name})


        else:
            messages.error(request, "Wrong Credentials")
            return redirect('home')



    return render(request, 'authentication/signin.html')
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']


        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = name
        myuser.save()

        messages.success(request, "Your account created successfully")

        return redirect('signin')

    return render(request, 'authentication/signup.html')
def signout(request):
    pass