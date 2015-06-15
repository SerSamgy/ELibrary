from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.http import require_GET, require_http_methods

from .decorators import ban_check
from .forms import BookSearchForm, LibraryUserCreationForm
from .models import Book


@require_GET
def home(request):
    """
    Standard root page.

    :param request: GET request
    :return:        Rendered HTML page
    """
    return render(request, "library/base_library.html")


@require_http_methods(['GET', 'POST'])
def books(request):
    """
    Page with search form. Returns search results to table.

    :param request: GET/POST request
    :return:        HTML page with search form and list of found books
    """
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
                if svalue:
                    skwargs[skey] = svalue
            # filter with empty kwargs returns all values from db
            # we don't need it
            if skwargs:
                books = Book.objects.filter(**skwargs)
    else:
        form = BookSearchForm()
    args['form'] = form
    args['books'] = books
    return render(request, "library/library_search.html",
                  context=args)


@ban_check
@require_GET
def book(request, pk):
    """
    Page with embed book file to read. Checks if user is banned.
    If it's true, shows error message and blocks content from user.

    :param request: GET request
    :param pk:      Primary key to book record
    :return:        HTML page with embedded (wrapped in <embed> tag) book file
                    or 404 if record hasn't been found
    """
    book = get_object_or_404(Book, id=pk)
    return render(request, "library/library_embed_book.html",
                  context={'book': book})


@require_http_methods(['GET', 'POST'])
def register(request):
    """
    Standard registration form. Redirects to root page on success.

    :param request: GET/POST request
    :return:        Rendered form
    """
    args = {}
    if request.method == 'POST':
        form = LibraryUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Вы успешно прошли регистрацию!'))
            return HttpResponseRedirect(reverse('home'))
    else:
        form = LibraryUserCreationForm()
    args['form'] = form
    return render(request, "library/library_registration.html", context=args)
