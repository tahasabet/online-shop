from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms
from .models import Profile


class UpdateUserInfo(forms.ModelForm):
    phone = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone number'}))
    address = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}))
    city = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}))
    state = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'}))
    zipcode = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zipcode'}))
    country = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'country'}))


    class Meta:
        model = Profile
        fields = ('phone','address','city','state','zipcode','country')



class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'name': 'pwd'})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'name': 'pwd'})
    )



    class Meta:
        model = User
        fields = ['New_Password1','New_Password2']



class UpdateUserForm(UserChangeForm):
    first_name = forms.CharField(required=False,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(required=False,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(required=False,
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    username = forms.CharField(required=False,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')







class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'name': 'pwd'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'name': 'pwd'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
