# from django import forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'field',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'field space',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email_address', 'password1', 'password2')

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'field',
    }))
    email_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email Address',
        'class': 'field',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'field space',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'field space',
    }))


from django import forms
from catalog.models import Seller, Donator

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

from django import forms
from catalog.models import Seller

class DonatorForm(forms.ModelForm):
    class Meta:
        model = Donator
        fields = '__all__'

