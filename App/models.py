from django.db import models

#_________________________________________

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'
#___________________________
class Bk(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=255)
    published = models.DateField()
    publisher = models.CharField(max_length=255)
    pages = models.IntegerField()
    description = models.TextField()
    website = models.URLField()
    

    def __str__(self):
        return self.title
# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    description=models.CharField(max_length=255)



def __str__(self):
    return f"{self.title}{self.author}{self.description}"