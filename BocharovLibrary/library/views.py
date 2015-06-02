from django.shortcuts import render


def home(request):
    return render(request, "library/base_library.html")
