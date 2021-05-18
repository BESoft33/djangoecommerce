from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def login(request):
    if request.user.is_authenticated:
            return redirect('/')
    else:
        return render(request, 'login.html')

def logout(request):
    pass

def signup(request):
    pass