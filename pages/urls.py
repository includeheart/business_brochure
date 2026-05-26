from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]