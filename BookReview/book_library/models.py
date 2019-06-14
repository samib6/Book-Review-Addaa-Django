from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    start_date = models.DateField()#date when you started reading the book
    end_date = models.DateField()#date you finished reading it.
    genre = models.ManyToManyField(Category)
    book_review = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review_detail',args=(self.id,))
