from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html', {'password':'daohofqooqweq'} )

def password(request):
    thepassword = ''
    letters = 'abcdefghijklmnopqrstuvwyxz'
    characters = list(letters)
    if request.GET.get('uppercase'):
        characters.extend(list(letters.upper()))
    if request.GET.get('special-characters'):
        characters.extend(list('!@#$%^&*()_'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    for x in range(length):
        thepassword += random.choice(characters)
        x =x+1
    return render(request, 'generator/password.html',{'password':thepassword})

def aboutus(request):
    return render(request, 'generator/aboutus.html')
# Create your views here.
