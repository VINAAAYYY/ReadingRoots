# Create your views here.

from books.models import book
from os import name
from django.http import HttpResponse, request
from django.shortcuts import render
from .models import book

gen = []
lang = []

def index(request):
    #return render(request, 'homepage.html')
    param = book.objects.all()
    for a in param:
        if a.genre not in gen:
            if len(a.genre)==0:
                continue
            gen.append(a.genre)
        if a.language not in lang:
            if len(a.language)==0:
                continue
            lang.append(a.language)
    return render(request, 'books/homepage.html', {'param':param, 'gen':gen, 'lang':lang})

def add_book(request):
    return render(request, 'books/add_books.html')

def added(request):
    name = request.GET.get('Book name', '')
    genre = request.GET.get('Genre', '')
    language = request.GET.get('Language', '')
    author = request.GET.get('Author', '')
    new_book = book(book_name=name, genre=genre, author=author, language=language)
    new_book.save()
    return HttpResponse('''your book is added<br><a href='../'>go back</a><br><a href='../../'>Homepage</a>''')

def apply(request):
    filtration = []
    genre_needed = []
    lang_needed = []
    for a in gen:
        check = request.GET.get(a, 'off')
        if(check=='on'):
            genre_needed.append(a)
            for books in book.objects.filter(genre=a):
                filtration.append(books)
    for a in lang:
        check = request.GET.get(a, 'off')
        if(check=='on'):
            lang_needed.append(a)
            for books in book.objects.filter(language=a):
                if(books not in filtration):
                    if(books.genre in genre_needed):
                        filtration.append(books)
    for a in filtration:
        if(a.language not in lang_needed):
            filtration.remove(a)
    
    return render(request, 'books/applying.html', {'filtration':filtration})