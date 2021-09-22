from django.shortcuts import render

def index(request):
    return render(request, 'app/base.html')


def about(request):
    return render(request, 'app/about.html')


def about2(request):
    return render(request, 'app/about2.html')

def service(request):
    return render(request, 'app/service-layout1.html')

def products(request):
    return render(request, 'app/products.html')

def blog(request):
    return render(request, 'app/blog.html')

def pricing(request):
    return render(request, 'app/pricing.html') 