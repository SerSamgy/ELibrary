from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import BookSearchForm


@require_GET
def home(request):
    return render(request, "library/base_library.html")

@require_http_methods(['GET', 'POST'])
def books(request):
    form = BookSearchForm()
    return render(request, "library/library_search.html", context={'form': form})
