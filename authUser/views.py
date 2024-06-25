from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm

from authUser.forms import UserRegistrationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}")
            print(f"User {username} authenticated successfully.")  # Debug message
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            print("Authentication failed. Invalid username or password.")  # Debug message
    else:
        print("Request method is not POST.")  # Debug message
    return render(request, 'authentications/login.html')


def home(request):
    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    print(f"User logged out successfully.")  # Debug message
    return redirect('login')



           
def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcome {username}")
            print(f"User {username} registered and logged in successfully.")  # Debug message
            return redirect('home')  # Change this line to redirect to home page
    else:
        form = UserRegistrationForm()
    return render(request, 'authentications/register.html', {'form': form})
