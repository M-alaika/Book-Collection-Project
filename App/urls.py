from django.urls import path
from . import views
urlpatterns=[
    path('',views.main,name='main'),

    path('contact/', views.contact, name='contact'),


    path('books/', views.book_list_view, name='json'),
    path('bbooks/', views.book_list_viiew, name='book_list'),

    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('bookss/',views.bookss,name='bookss'),
    path('testing/',views.testing,name='testing'),
    path('BOOK/',views.BOOK,name='BOOK'),
    path('BOOK/details/<int:id>',views.details, name='details'),
]