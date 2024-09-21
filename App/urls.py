from django.urls import path
from . import views
urlpatterns=[
    path('',views.main,name='main'),
    path('testing/',views.testing,name='testing'),
    path('BOOK/',views.BOOK,name='BOOK'),
    path('NBOOK/',views.NBOOK,name='NBOOK'),
    # path('FBOOK/',views.FBOOK,name='FBOOK'),
    path('BOOK/details/<int:id>',views.details, name='details'),
    path('NBOOK/ndetails/<int:id>',views.ndetails, name='ndetails'),
]