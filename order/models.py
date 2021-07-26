from django.db import models

from main.models import Book


class Order(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='orders')
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=25)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.email} - {self.phone}'
