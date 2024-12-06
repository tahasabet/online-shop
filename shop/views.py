from itertools import product

from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm,UpdateUserForm,UpdatePasswordForm,UpdateUserInfo
from django.db.models import Q


from django.contrib import messages
from django.db.models import Q
from .models import Product

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '').strip()
        if searched:
            searched_products = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

            if searched_products.exists():
                return render(request, 'search.html', {'searched': searched_products})
            else:
                messages.info(request, 'No products found for your search.')
        else:
            messages.warning(request, 'Please enter a search term.')
        return render(request, 'search.html', {'searched': []})
    return render(request, 'search.html', {})




def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UpdateUserInfo(request.POST or None,instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, 'your information has been updated')
            return redirect('home')

        return render(request,'update_info.html',{'form':form})
    else:
        messages.error(request, 'You are not logged in')
        return redirect('login')


def category_summary(request):
    all_cat = Category.objects.all()

    return render(request, 'category_summary.html',{'category':all_cat})



def helloworld(request):
    all_products = Product.objects.all()
    return render(request,'index.html',{'products':all_products})

def about(request):
    return render(request,'about.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'You are now logged in')
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')



def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out')
    return redirect("home")


def signup_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            if user:
                login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('home')
            else:
                messages.error(request, 'Authentication failed. Please contact support.')
                return redirect('login')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    return render(request, 'signup.html', {'form': form})



def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None,instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'Your account has been updated!')
            return redirect('home')

        return render(request,'update_user.html',{'user_form':user_form})
    else:
        messages.error(request, 'You are not logged in')
        return redirect('login')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = UpdatePasswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been updated!')
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                return redirect('update_password')

        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.success(request, 'You are not logged in')
        return redirect('login')




def product(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product.html', {'product': product})


def category(request,cat):
    cat = cat.replace('-','')
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products,"category":category})
    except:
        messages.success(request,'Category does not exist')
        return redirect('home')

