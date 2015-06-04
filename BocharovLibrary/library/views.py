from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import BookSearchForm
from .models import Book


@require_GET
def home(request):
    return render(request, "library/base_library.html")

@require_http_methods(['GET', 'POST'])
def books(request):
    args = {}
    books = None
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            skwargs = {}
            for field in form.fields:
                svalue = form.cleaned_data[field]
                if field != 'genre':
                    # according to this doc:
                    # https://docs.djangoproject.com/en/1.8/ref/databases/#sqlite-string-matching
                    # there is a slight difference between case-sensitive and
                    # case-insensitive searches
                    skey = "%s__icontains" % field
                else:
                    # since 'genre' field is a ForeignKey, we need to pass
                    # another field to search in
                    skey = "%s__title__icontains" % field
                if svalue: skwargs[skey] = svalue
            # filter with empty kwargs returns all values from db
            # we don't need it
            if skwargs: books = Book.objects.filter(**skwargs)
    else:
        form = BookSearchForm()
    args['form'] = form
    args['books'] = books
    return render(request, "library/library_search.html",
                  context=args)

@login_required
@require_GET
def book(request, pk):
    book = Book.objects.filter(id=pk)[0]
    return render(request, "library/library_embed_book.html",
                  context={'book': book})
