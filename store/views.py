from django.shortcuts import render

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

