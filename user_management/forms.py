from django import forms
from .models import User
from django.contrib.auth.models import User


from .models import User, SecurityQuestion

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'security_question', 'security_answer']
        widgets = {
            'password': forms.PasswordInput(),
        }

class PasswordChangeForm(forms.Form):
    security_question = forms.ModelChoiceField(queryset=SecurityQuestion.objects.all())
    security_answer = forms.CharField(max_length=100, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class AdminPasswordChangeForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("New Password and Confirm Password do not match.")

        return cleaned_data

# forms.py

from django import forms
from django.contrib.auth.models import User

class AdminPasswordChangeForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select User")
    security_question = forms.ChoiceField(choices=[
        ('1', 'What is your pet  name?'),
        ('2', 'What is your favorite color?'),
        # Add more security questions here as needed
    ], widget=forms.Select(attrs={'class': 'form-control'}))
    security_answer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
