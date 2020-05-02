from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book
# Create your views here.

def book_list(request):

    all_books = Book.objects.order_by('rank')
    paginator = Paginator(all_books, 3)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    context = {'page': page, 'books': books }
    return render(request, 'book/book_list.html', context)

def book_detail(request, id):
    book = Book.objects.filter(pk=id)
    print(book)
    return render(request, 'book/book_details.html', {'book': book[0]})