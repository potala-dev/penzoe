from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import BookUploadForm
from .models import Book
from .utils import handle_uploaded_file


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


@login_required
def upload_book(request):
    if request.method == "POST":
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            file_name, download_url = handle_uploaded_file(cd["file"], cd["title"])
            # create Book object
            Book.objects.create(
                title=cd["title"],
                author=cd["author"],
                download_link=download_url,
                genre=cd["genre"],
                file_name=file_name,
            )
            print("book created")
            return HttpResponseRedirect("/")
    else:
        form = BookUploadForm()
    return render(request, "book/book_upload_form.html", {"form": form})
