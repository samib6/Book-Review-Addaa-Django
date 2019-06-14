from django.shortcuts import render
from book_library.models import Book
# Create your views here.
def Index(request):
    return render(request,'pages/index.html')
