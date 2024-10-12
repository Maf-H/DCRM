from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # check if person is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POSR['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been logged in")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in, Try again... ")
            return redirect('home')
    else:
        return render(request,"home.html", {})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have been logged out...")
    return redirect('home')
def register_user(request):
    return render(request,"register.html", {})

