from django.contrib.auth.decorators import login_required
from .forms import DonatorForm, SignupForm, LoginForm
from catalog.models import Category, Catalogue
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from catalog.models import Category, Catalogue
from django.contrib.auth import authenticate, login
from catalog.models import Catalogue,Seller, Donator
# from catalog.models import 

def search_catalogue(request):
    query = request.GET.get('q')
    catalogues = Catalogue.objects.filter(name__icontains=query)
    return render(request, 'catalog.html', {'catalogues': catalogues, 'query': query})

@login_required
def catalogue(request):
    username = request.user.username
    catalogues = Catalogue.objects.filter(is_sold=False)
    categories = Category.objects.all()

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        catalogues = catalogues.filter(price__gte=min_price, price__lte=max_price)

    sell_or_donate = request.GET.get('sell_or_donate')
    if sell_or_donate:
        catalogues = catalogues.filter(sell_or_donate=sell_or_donate)

    return render(request, 'core/catalog.html', {
        'categories': categories,
        'catalogues': catalogues,
        'username': username,
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful! Login to continue.')
            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("User:", user)  
        if user is not None:
            print("User authenticated successfully!")  
            login(request, user)
            print("User logged in successfully!") 
            return redirect('/account')  
        else:
            print("Invalid username or password!")  
            return render(request, 'core/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'core/login.html', {})

def index(request):
    return render(request, "core/index.html")

def chat(request):
    return render(request, "core/chat.html")

def catalog(request):
    return render(request, "core/catalog.html")

@login_required
def checkout(request):
    username = request.user.username
    return render(request, "core/checkout.html", {'username': username})


def donate(request):
    username = request.user.username
    return render(request, "core/donating.html", {'username': username})


def orders(request):
    username = request.user.username
    categories = Category.objects.all()
    for category in categories:
        category.num_items = Catalogue.objects.filter(category=category).count()
    return render(request, "core/orders.html", {'username': username, 'categories': categories})

@login_required
def account(request):
    print("Account view function called")
    username = request.user.username
    # email_address = a.user.email_address
    print("Username:", username)
    return render(request, 'core/account.html', {'username': username})

@login_required
def donating(request):
    username = request.user.username
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = DonatorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your donation! Your book will be added to the catalog after verification. Until then, happy browsing!')
            return redirect('/catalog') 
        else:
            # If the form is not valid, render the form again with the errors
            return render(request, 'core/donating.html', {'form': form, 'username': username, 'categories': categories, 'error_message': 'Invalid details'})
    else:
        # If the request method is not POST, render the form with a new empty form
        form = DonatorForm()
        return render(request, 'core/donating.html', {'form': form, 'username': username, 'categories': categories})

# views.py
from django.shortcuts import render, redirect
from .forms import SellerForm
from django.http import HttpResponseBadRequest

@login_required
def selling(request):
    username = request.user.username
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contributing to sustainability by listing your book for resale! Your book will be added to the catalog after verification. Until then, happy browsing!')
            return redirect('/catalog') 
        else:
            # If the form is not valid, render the form again with the errors
            return render(request, 'core/selling.html', {'form': form, 'username': username, 'categories': categories, 'error_message': 'Invalid details'})
    else:
        # If the request method is not POST, render the form with a new empty form
        form = SellerForm()
        return render(request, 'core/selling.html', {'form': form, 'username': username, 'categories': categories})
