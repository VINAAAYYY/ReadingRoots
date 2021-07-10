# Create your views here.

from django.http.response import FileResponse
from books.models import book
from os import name
from django.http import HttpResponse, request
from django.shortcuts import render
from .models import book

gen = []
lang = []

def hyphen(string):
    string =  string.replace("\n", "")
    string =  string.replace(" ", "-")
    return string.lower()
    
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
    genre = hyphen(genre)
    language = request.GET.get('Language', '')
    language = hyphen(language)
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
        print('for a = ', a, 'check is ', check)
        if(check=='on'):
            genre_needed.append(a)
            for books in book.objects.filter(genre=a):
                filtration.append(books)
    for a in lang:
        check = request.GET.get(a, 'off')
        if(check=='on'):
            lang_needed.append(a)
            for books in book.objects.filter(language=a):
                if len(genre_needed)==0:
                    filtration.append(books)
                elif(books not in filtration):
                    if(books.genre in genre_needed):
                        filtration.append(books)
     
    if(len(lang_needed)!=0):
        for a in filtration:
            if(a.language not in lang_needed):
                filtration.remove(a)
                print(a)
    
    return render(request, 'books/applying.html', {'filtration':filtration})