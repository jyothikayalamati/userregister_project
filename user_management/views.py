from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import AdminPasswordChangeForm, PasswordChangeForm, UserRegistrationForm

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with your login URL name
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html', {'form': form})

def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            security_question = form.cleaned_data['security_question']
            security_answer = form.cleaned_data['security_answer']
            new_password = form.cleaned_data['new_password']
    
          

            # Check if the security question and answer match the user's details
    user = User.objects.get(security_question=security_question, security_answer=security_answer)
    if user:
                user.password = new_password
                user.save()
                return redirect('login')  # Replace 'login' with your login URL name
    form = PasswordChangeForm()
    return render(request, 'password_change.html', {'form': form})


def admin_password_change_view(request):
    

    if request.method == 'POST':
        form = AdminPasswordChangeForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user']
            new_password = form.cleaned_data['new_password']

            user = User.objects.get(pk=user_id)
            user.set_password(new_password)
            user.save()
            return redirect('login')  # Redirect to login page on successful password change
    else:
        form = AdminPasswordChangeForm()

    return render(request, 'admin_password_change.html', {'form': form, })