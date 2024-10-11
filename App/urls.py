from django.urls import path
from . import views


from django.urls import path
from .views import contact_view
from django.http import HttpResponse
urlpatterns=[
    path('',views.main,name='main'),

     path('contact/', contact_view, name='contact'),
    path('success/', lambda request: HttpResponse("Message sent!"), name='success'),

    # path('contact/', views.contact, name='contact'),


    path('books/', views.book_list_view, name='json'),
    path('bbooks/', views.book_list_viiew, name='book_list'),

    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('bookss/',views.bookss,name='bookss'),
    path('testing/',views.testing,name='testing'),
    path('BOOK/',views.BOOK,name='BOOK'),
    path('BOOK/details/<int:id>',views.details, name='details'),
]