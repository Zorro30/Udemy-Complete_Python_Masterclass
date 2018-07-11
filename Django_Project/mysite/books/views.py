'''
from django.shortcuts import render
from .models import Books
#from django.template import loader
from django.shortcuts import render
from django.http import Http404
# Create your views here.

from django.http import HttpResponse

def index(request):
    all_books = Books.objects.all()
    context = {
        'all_books' : all_books
    }
     
    return render(request,'books/index.html',context)

def detail(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
    except Books.DoesNotExist:
        raise Http404('This book does not exist')
    return render(request,'books/detail.html',{'book':book})
    '''

#============= Using GENERIC VIEWS==========================
from django.views import generic
from .models import Books
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Books.objects.all()

class BookCreate(CreateView):
    model = Books
    fields = ['name','author','price','type','book_image']

class DetailView(generic.DetailView):
    model = Books
    template_name = 'books/detail.html'


