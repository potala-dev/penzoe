from django.shortcuts import redirect, render

from book.models import Book

from .forms import ThreadForm
from .models import Thread


def book_threads(request, id):
    form = ThreadForm()
    threads = Thread.objects.filter(book__id=id)
    book_title = request.GET.get("book_title")
    context = {
        "threads": threads,
        "form": form,
        "book_id": id,
        "book_title": book_title,
    }
    return render(request, "discourse/book_threads.html", context)


def create_thread(request, id):
    form = ThreadForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        book = Book.objects.get(pk=id)
        print(book.title)
        Thread.objects.create(
            user=request.user, book=book, title=cd["title"], body=cd["body"]
        )
        return redirect(book)
