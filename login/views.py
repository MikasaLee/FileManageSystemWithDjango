from django.shortcuts import render
from .models import userLogin
# Create your views here.

def login(request):
    return render(request, "login.html")

def logout(request):
    if request.session.has_key('username'):
        del request.session['username']
    return render(request, "login.html")