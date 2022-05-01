from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'masdfklmksdfmlasd'})

def about(request):
    thepassword='testing'
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length=request.GET.get('length',50)
    length2=int(length)
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    characters.extend(list('1234567890'))
    characters.extend(list('!@#$%^&*()_+-='))
    thepassword=''
    for x in range(length2+1):
        thepassword+=random.choice(characters)
    return render(request, 'generator/about.html', {'examplepassword': thepassword})










def password(request):

    thepassword='testing'
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length=request.GET.get('length',1)
    length2=int(length)
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_+-='))


    thepassword=''
    for x in range(length2+1):
        thepassword+=random.choice(characters)
    return render(request, 'generator/password.html',{'password':thepassword})