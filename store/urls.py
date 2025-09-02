


from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('casestudies/', views.casestudies, name='casestudies'),
    path('consultance/', views.consultance, name='consultance'),
    path('ux/', views.ux, name='ux'),
    path('ecommerce/', views.ecommerce, name='ecommerce'),
    path('atpohor/', views.atpohor, name='atpohor'),
    path('baby/', views.baby, name='baby'),


    
]

