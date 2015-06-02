from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', view=views.home, name='home'),
    url(r'^books/', view=views.books, name='books'),
    url(r'^book/(?P<pk>\d+)/$', view=views.book, name='book'),
]