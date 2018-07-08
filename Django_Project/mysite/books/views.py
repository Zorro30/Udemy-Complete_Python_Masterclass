from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h>This is the books homepage!</h>")

def detail(request, book_id):
    return HttpResponse("<h2> Details for Book ID:" +str(book_id)+ "</h2>")