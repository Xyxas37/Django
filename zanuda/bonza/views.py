from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(reguest):
    return render(reguest, 'bonza/index.html')

def data(reguest):
    return render(reguest, 'bonza/data.html')


def test(reguest):
    return render(reguest, 'bonza/test.html')

def works(request):
    return render(request, 'bonza/works.html')

def contacts(request):
    return render(request, 'bonza/contacts.html')

def payments(request):
    return render(request, 'bonza/payments.html')

def login_view(request):
    return render(request, 'bonza/login.html')

def register_view(request):
    return render(request, 'bonza/register.html')

def logout_view(request):
    return render(request, 'bonza/logout.html')