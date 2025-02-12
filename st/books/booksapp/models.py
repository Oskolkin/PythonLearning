from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(auto_now=True)

class Genre(models.Model):
    name = models.CharField(max_length=256) 

class Book(models.Model):
    name = models.CharField(max_length=256) 
    published_date = models.DateField(blank=True, null=True) 
    author = models.ForeignKey(Author, models.PROTECT)
    genres = models.ManyToManyField(Genre)

class BookInstance(models.Model):
    book = models.ForeignKey(Book, models.CASCADE)
    STATUSES = [
        ('t', 'Taken'),
        ('m', 'Maintenance'),
        ('a', 'Available')
    ]
    status = models.CharField(max_length=1, choices=STATUSES)
