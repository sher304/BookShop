from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='authors')

    def __str__(self):
        return f'{self.name} {self.surname}'

class Genre(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):

    CHOICES = (
        ('in stock', 'В наличии'),
        ('out of stock', 'Нет в наличии')
    )

    title = models.CharField(max_length=60)
    image = models.ImageField(blank=True, null=True, upload_to='books')
    status = models.CharField(choices=CHOICES, max_length=25)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='books')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('home')
