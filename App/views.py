from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from App.models import Book
# from App.models import FBook
from App.models import NBook
# Create your views here.
def BOOK(request):
        books=Book.objects.all().values()
        template=loader.get_template('BOOK.html')
        context={
            'books':books,
        }
        return HttpResponse(template.render(context,request))
def NBOOK(request):
        nbooks=NBook.objects.all().values()
        template=loader.get_template('NBOOK.html')
        context={
            'nbooks':nbooks,
        }
        return HttpResponse(template.render(context,request))
# def FBOOK(request):
#         fbooks=FBook.objects.all().values()
#         template=loader.get_template('FBOOK.html')
#         context={
#             'Fbooks':fbooks,
#         }
#         return HttpResponse(template.render(context,request))
def details(request,id):
    book=Book.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'book':book,
    }
    return HttpResponse(template.render(context,request))
def ndetails(request,id):
    nnbook=NBook.objects.get(id=id)
    template=loader.get_template('ndetails.html')
    context={
        'nnbook':nnbook,
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