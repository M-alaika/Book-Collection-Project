from django.contrib import admin
from .models import Book


from django.contrib import admin
from .models import Message

class MemberAdmin(admin.ModelAdmin):
    list_display=("name","email","message",)
admin.site.register(Message,MemberAdmin)
# admin.site.register(Message)
# Register your models here.
# class MemberAdmin(admin.ModelAdmin):
#     list_display=("title","author","description",)
# admin.site.register(Book,MemberAdmin)
