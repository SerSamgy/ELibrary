from django.conf.urls import url
from django.contrib.auth.views import login as auth_login, \
    logout as auth_logout

from .forms import LibraryLoginForm
from . import views


urlpatterns = [
    url(r'^$', view=views.home, name='home'),
    url(r'^books/', view=views.books, name='books'),
    url(r'^book/(?P<pk>\d+)/$', view=views.book, name='book'),
    url(r'^login/', auth_login, {"template_name": "library/library_login.html",
                                 "authentication_form": LibraryLoginForm},
        name='login'),
    url(r'^logout/', auth_logout,
        {"template_name": "library/library_logout.html"}, name='logout')
]