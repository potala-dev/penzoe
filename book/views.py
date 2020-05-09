from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import BookUploadForm
from .models import Book


def book_list(request,):
    all_books = Book.objects.order_by("-rank")
    paginator = Paginator(all_books, 1)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {"page": page_request_var, "books": paginated_queryset}
    return render(request, "book/book_list.html", context)


def book_detail(request, id):
    book = Book.objects.filter(pk=id)
    print(book)
    return render(request, "book/book_details.html", {"book": book[0]})


def book_by_cat(request, cat):
    if cat:
        all_books = Book.objects.filter(genre=cat).order_by("-rank")
    else:
        all_books = Book.objects.order_by("-rank")
    paginator = Paginator(all_books, 1)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {"page": page_request_var, "books": paginated_queryset}
    return render(request, "book/book_list.html", context)


def upload_book(request):
    if request.method == "POST":
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            handle_uploaded_file(request.FILES["file"])
            print(cd)
            return HttpResponseRedirect("/")
    else:
        form = BookUploadForm()
    return render(request, "book/book_upload_form.html", {"form": form})


def handle_uploaded_file(f):
    with open("./test-book.pdf", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
