from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import BookSearchForm
from .models import Book


@require_GET
def home(request):
    return render(request, "library/base_library.html")

@require_http_methods(['GET', 'POST'])
def books(request):
    form = BookSearchForm()
    books = Book.objects.filter(id=1) # TODO: delete this!
    return render(request, "library/library_search.html",
                  context={'form': form, 'books': books})

@require_GET
def book(request, pk):
    book = Book.objects.filter(id=pk)[0]
    return render(request, "library/library_embed_book.html",
                  context={'book': book})
