from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Category,Book

class ReviewCreate(CreateView):
    model = Book
    fields = ['title','author','start_date','end_date','genre','book_review']
    #default template used by CreateView is <app>/<model>_form.html

class ReviewList(ListView):
    model = Book
    template_name = "book_library/book_list.html"
    queryset = Book.objects.all()
    context_object_name = 'queryset'

class ReviewDetail(DetailView):
    model = Book
    template_name = "book_library/review_detail.html"

class ReviewDelete (DeleteView):
    model = Book
    success_url = reverse_lazy('bookreview_list')
