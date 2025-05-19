'''from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by('title')
    paginator = Paginator(books, 5)  # 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_obj': page_obj})'''

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def book_list(request):
    author = request.GET.get('author', '')
    year = request.GET.get('year', '')
    per_page = int(request.GET.get('per_page', 10))
    page_number = request.GET.get('page', 1)

    books = Book.objects.all()
    if author:
        books = books.filter(author__icontains=author)
    if year:
        books = books.filter(published_year=year)

    paginator = Paginator(books, per_page)
    page_obj = paginator.get_page(page_number)

    # Add the list to context
    per_page_options = [5, 10, 20, 50]

    return render(request, 'books/book_list.html', {
        'page_obj': page_obj,
        'per_page_options': per_page_options,
    })
