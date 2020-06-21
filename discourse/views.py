from django.shortcuts import redirect, render

from book.models import Book

from .forms import ThreadForm
from .models import Thread


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
