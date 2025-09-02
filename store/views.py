
from django.shortcuts import render

def contact_success_view(request):
    return render(request, 'contact/success.html')
def homePage(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "aboutus.html")

def services(request):
    return render(request, "services.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")
def portfolio(request):
     return render(request, "portfolio.html")
def casestudies(request):
     return render(request, "casestudies.html")
def ux(request):
     return render(request, "ux.html")
def consultance(request):
     return render(request, "consultance.html")
def ecommerce(request):
     return render(request, "ecommerce.html")

def atpohor(request):
     return render(request, "atpohor.html")

def baby(request):
     return render(request, "baby.html")