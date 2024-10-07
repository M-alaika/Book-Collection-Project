from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.models import Book
# Create your views here.
import os
import json
from django.conf import settings
from django.shortcuts import render
#contact form


#___________________________
def book_list_viiew(request):
    file_path = os.path.join(settings.BASE_DIR, 'App', 'space_technology_books.json')
    with open(file_path) as f:
        data = json.load(f)

    # Sort books by rating in descending order
    books = sorted(data['bk'], key=lambda x: x['rating'], reverse=True)

    context = {
        'books': books,
    }
    return render(request, 'book_list.html', context)

#111111111111111
def book_list_view(request):
    file_path = os.path.join(settings.BASE_DIR, 'App', 'books.json')
    with open(file_path) as f:
        data = json.load(f)

    # Sort books by rating in descending order
    books = sorted(data['bk'], key=lambda x: x['rating'], reverse=True)

    context = {
        'books': books,
    }
    return render(request, 'book_list.html', context)
#bbbbbbbbbbbbbbb
# def load_json_dataa():
#     json_file_path = os.path.join(settings.BASE_DIR, 'App', 'space_technology_books.json')
#     with open(json_file_path, 'r', encoding='utf-8') as f:
#         return json.load(f)

# def book_list_vieww(request):
#     data = load_json_dataa()
#     books = data['bk']
#     return render(request, 'json.html', {'books': books})

#aaaaaaaaaaaaaaaaaaaaaaaaa

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())
def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())
def bookss(request):
    template=loader.get_template('json.html')
    return HttpResponse(template.render())
def BOOK(request):
        books=Book.objects.all().values()
        template=loader.get_template('BOOK.html')
        context={
            'books':books,
        }
        return HttpResponse(template.render(context,request))

def details(request,id):
    book=Book.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'book':book,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render()) 

def testing(request):
  #for decending order using - with age
  mydata = Book.objects.all().order_by('title')
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))