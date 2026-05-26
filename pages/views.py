"""Views for the pages app."""
from django.shortcuts import render

def home(request):
    """Render the home page."""
    return render(request, 'pages/home.html')

def about(request):
    """Render the about page."""
    return render(request, 'pages/about.html')

def services(request):
    """Render the services page."""
    return render(request, 'pages/services.html')

def contact(request):
    """Render the contact page."""
    return render(request, 'pages/contact.html')
