from os.path import join, abspath, dirname

from django.apps import AppConfig


class LibraryConfig(AppConfig):
    name = 'library'
    verbose_name = 'Bocharov Library'
    path = join(abspath(dirname(__file__)))