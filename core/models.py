from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    publication_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True, verbose_name='active book')

    def __str__(self):
        return self.title


class Reviewer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


# Yorum modeli
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )

    def __str__(self):
        return f'Review for {self.book.title} by {self.reviewer.username}'
