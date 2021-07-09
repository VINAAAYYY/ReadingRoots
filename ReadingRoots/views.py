from os import name
from django.http import HttpResponse, request
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    #return render(request, 'homepage.html')
    return redirect('/books')
