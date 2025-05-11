from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Product

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def signin(request):
    return render(request, 'signin.html')
