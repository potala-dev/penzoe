from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from book.models import Book

from .forms import CommentForm, ThreadForm
from .models import Comment, Thread


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


@login_required
def create_thread(request, id):
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            book = Book.objects.get(pk=id)
            thread = Thread(
                user=request.user, book=book, title=cd["title"], body=cd["body"]
            )
            thread.save()
            return redirect(thread)

    form = ThreadForm()
    context = {"form": form}

    return render(request, "discourse/thread_form.html", context)


def thread_comments(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            thread = Thread.objects.get(pk=id)
            Comment.objects.create(user=request.user, thread=thread, text=cd["text"])

    form = CommentForm()
    comments = Comment.objects.filter(thread__id=id)
    if not comments:
        thread = Thread.objects.get(pk=id)
    else:
        thread = comments[0].thread
    context = {"thread": thread, "comments": comments, "form": form}
    return render(request, "discourse/thread_comments.html", context)
