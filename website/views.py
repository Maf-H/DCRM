from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()
    # check if person is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
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
        return render(request,"home.html", {'records':records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have been successfully Registered...")
            messages.success(request, f"Account created for {username}!")
            return redirect('home')
        else:
            return render(request, "register.html", {'form': form})
        
    else:
        form = SignupForm()
        return render(request,"register.html", {'form': form})
     
    return render(request,"register.html", {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=pk)
        return render(request,"record.html", {'customer_record': customer_record})
    else:
        messages.success(request, f"You must be logged in to view that page!")
        return redirect('home')
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, f"Record deleted successefully")
        return redirect('home')
    else:
        messages.success(request, f"You must be logged in to delete a record!")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added.")
                return redirect("home")
        return render(request,"add_record.html", {'form':form})
    else:
        messages.success(request, f"You must be logged in to add a record!")
        return redirect('home')
