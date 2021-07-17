from django import forms
from django.contrib.auth.models import User
from .models import UserBase
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm, SetPasswordForm)

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Account email (cannot be changed)', max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}
    ))
    user_name =forms.CharField(label='Username',min_length=4, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-username','readonly': 'readonly'}
    ))
    first_name = forms.CharField(label='First Name', min_length=4, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'First Name', 'id': 'form-firstname'
        }))
    phone_number = forms.CharField(label='Phone Number', min_length=10, max_length=10, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Phone Number', 'id': 'form-phone'
        }))
    address_line_1 = forms.CharField(label='Address Line 1', max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Address Line 1', 'id': 'form-address-1'
        }))
    address_line_2 = forms.CharField(label='Address Line 2', max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Address Line 2', 'id': 'form-address-2'
        }))
    post_code = forms.CharField(label='Pin Code', max_length=10, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'Pin Code', 'id': 'form-pincode'
        }))
    town_city = forms.CharField(label='City', min_length=4, max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control mb-3', 'placeholder': 'City', 'id': 'form-city'
        }))
    class Meta:
        model = UserBase
        fields = ('email','user_name','first_name','phone_number', 'address_line_1','address_line_2','post_code','town_city')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False 
        self.fields['user_name'].required = True
        self.fields['email'].required = True

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'E-mail', 'id': 'login-username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'id': 'login-pwd'}
    ))


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'E-mail address is required'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields= ('user_name', 'email',)
    
    def clean_username(self):
        user_name = self.cleaned_data['username'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords do not match.")
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError("Please use another email. This email address is already taken")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update({
            'placeholder': "Username",
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'E-mail'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
        })

class PWDResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}
    ))
    def clean_email(self):
        email = self.cleaned_data['email']
        u = UserBase.objects.filter(email=email)
        if not u:
            raise forms.ValidationEror(
                'Unfortunately we cannot find that email address'
            )
        return email

class PWDResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}
    ))
    new_password2 = forms.CharField(label='Confirm New Pasword', widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Confirm New Password', 'id': 'form-newpass-confirm'}
    ))