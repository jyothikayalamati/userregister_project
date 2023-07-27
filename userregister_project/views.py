
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect


def login_view(request):
    # Your view logic here
    return render(request, 'login.html')  # Assuming you have a template named 'login.html'
    # Your login view code here
def index(request):
    return render(request,'user_management/login.html')
def register_view(request):
    # Your view logic here
    return render(request, 'register.html')  # Assuming you have a template named 'register.html'


def password_change_view(request):
    # Your view logic here
    return render(request, 'password_change.html')  # Assuming you have a template named 'password_change.html'
def admin_password_change_view(request):
    # Your view logic here
    return render(request, 'admin_password_change.html')  # Assuming you have a template named 'admin_password_change.html'
def get_user_security_answer(request):
    # Your view logic here
    return render(request, 'get_user_security_answer.html')  # Assuming you have a template named 'get_user_security_answer.html'
@login_required
def special(request):
    return HttpResponse("you are logged in, congratulations!")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    # Check if the request method is POST, which means the user submitted the login form
    if request.method == 'POST':
        # Process the login form data here (e.g., validating credentials)
        # For simplicity, let's assume you have a valid_login function that returns True for a successful login:
        if login(request.POST['username'], request.POST['password']):
            # Redirect the user to a success page or dashboard
            return redirect('dashboard')  # 'dashboard' is the name of the URL pattern for the dashboard view
        else:
            # If login fails, display an error message or render the login page with an error context
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # If the request method is GET, display the login page
        return render(request, 'login.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS NOT IN ACTIVE STATE")
        else:
            print("some person tried to login and failed!")
            print("username:{} and password {}".format(username,password))
            return HttpResponse("invalid login details given!")
    
   
