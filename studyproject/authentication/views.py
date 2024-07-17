from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signup(request):  
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.gender = gender

        myuser.save()

        messages.success(request, "Your Account Has Been Created Successfully!")
        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):   
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully!")
            return redirect('main')  # Redirect authenticated users to the dashboard

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')        

    return render(request, "authentication/signin.html")

def signout(request):    
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

def main(request):
    if request.user.is_authenticated:
        fname = request.user.first_name
        return render(request, "dashboard/main.html", {'fname': fname})
    else:
        # Redirect to the signin page if the user is not logged in
        return redirect('signin')
