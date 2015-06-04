from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from fields import YearField


class YearModelField(models.IntegerField):
    "A model field for storing years, e.g. 2015"
    def formfield(self, **kwargs):
        defaults = {'form_class': YearField}
        defaults.update(kwargs)
        return super(YearModelField, self).formfield(**defaults)


class Genre(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Cities(models.Model):
    city_name = models.CharField(verbose_name=_("Название"), max_length=32)

    def __str__(self):
        return self.city_name


class Book(models.Model):
    author = models.CharField(_("Автор"), max_length=64)
    title = models.CharField(_("Заголовок"), max_length=255)
    genre = models.ForeignKey(Genre, verbose_name=_("Жанр"), null=True)
    year = YearModelField(_("Год издания"), null=True)
    publisher = models.CharField(_("Издательство"), max_length=64)
    pub_city = models.ForeignKey(Cities, verbose_name=_("Город издательства"),
                                 null=True)
    book_file = models.FileField(verbose_name=_("Загрузить"), upload_to='books/')

    def __str__(self):
        return "%s. %s" % (self.author, self.title)


# Manage User models
class LibraryUserManager(BaseUserManager):
    def create_user(self, login, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class LibraryUser(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(_("Логин"), max_length=24, unique=True)
    name = models.CharField(_("Имя"), max_length=255)
    email = models.EmailField(
        verbose_name=_('Email'),
        max_length=255,
        unique=True,
    )
    birth_year = YearModelField(_("Год рождения"), null=True)
    city = models.ForeignKey(Cities, verbose_name=_("Город"), null=True)
    sex = models.CharField(_("Пол"), max_length=1, default='M')
    banned = models.BooleanField(_("Забанен"), default=False)
    is_staff = models.BooleanField(_('Статус пользователя'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('Активный'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active.  Unselect this instead of deleting accounts.'))
    is_superuser = False
    date_joined = models.DateTimeField(_('Дата регистрации'),
                                       default=timezone.now)

    objects = LibraryUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.login

    def get_short_name(self):
        return self.login

    def __str__(self):
        return self.login