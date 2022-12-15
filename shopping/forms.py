from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.forms.widgets import PasswordInput, TextInput
from .models import customer,billing_details

class CustomerRegistration(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control '}))
    #add name address phone email
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control '}))
    username=forms.RegexField(regex=r'^[0-9]{10}$',label="Phone",widget=forms.TextInput(attrs={'class':'form-control '}))

    class Meta:
        model = User
        fields = ['username','name', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={"class": "form-control"})}


class Loginform(AuthenticationForm):
    username = UsernameField(label="Phone",widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class detailsform(forms.ModelForm):
    name=forms.RegexField(regex=r'^[a-zA-Z ]+$',label="Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control '}))
    address=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control '}))
    city=forms.RegexField(regex=r'^[a-zA-Z ]+$',label="City",widget=forms.TextInput(attrs={'class':'form-control '}))
    state=forms.RegexField(regex=r'^[a-zA-Z ]+$',label="State",widget=forms.TextInput(attrs={'class':'form-control '}))
    pin=forms.RegexField(regex=r'^[0-9]{6}$',label="Pin Code",widget=forms.TextInput(attrs={'class':'form-control '}))
    phone=forms.RegexField(regex=r'^[0-9]{10}$',label="Phone",widget=forms.TextInput(attrs={'class':'form-control '}))



    # name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    # email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control '}))
    # address=forms.CharField(label="Address",widget=forms.TextInput(attrs={'class':'form-control '}))
    # city=forms.CharField(label="City",widget=forms.TextInput(attrs={'class':'form-control '}))
    # state=forms.CharField(label="State",widget=forms.TextInput(attrs={'class':'form-control '}))
    # pin=forms.CharField(label="Pin Code",widget=forms.TextInput(attrs={'class':'form-control '}))
    # phone=forms.CharField(label="Phone",widget=forms.TextInput(attrs={'class':'form-control '}))
    class Meta:
        model=billing_details
        exclude=['user_id']
        fields=['name','email','address','city','state','pin','phone']
