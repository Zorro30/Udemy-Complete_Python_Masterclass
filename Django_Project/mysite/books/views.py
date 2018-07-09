from django.shortcuts import render
from .models import Books
# Create your views here.

from django.http import HttpResponse

def index(request):
    all_books = Books.objects.all()
    html = ''
    for book in all_books:
        url = "/books/" + str(book.id) + '/'
        html += '<a href="' + url + '">' +str(book.name)+ ' </a><br>' 
    return HttpResponse(html)

def detail(request, book_id):
    return HttpResponse("<h2> Details for Book ID:" +str(book_id)+ "</h2>")