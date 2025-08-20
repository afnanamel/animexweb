from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]

