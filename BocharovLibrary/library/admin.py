from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import LibraryUserChangeForm, LibraryUserCreationForm
from .models import LibraryUser, Book


USERNAME_FIELD = get_user_model().USERNAME_FIELD

REQUIRED_FIELDS = (USERNAME_FIELD,) + tuple(get_user_model().REQUIRED_FIELDS)

BASE_FIELDS = (None, {
    'fields': REQUIRED_FIELDS + ('password',),
})

SIMPLE_PERMISSION_FIELDS = (_('Permissions'), {
    'fields': ('is_active', 'banned', 'is_staff', 'is_superuser',),
})

DATE_FIELDS = (_('Important dates'), {
    'fields': ('last_login', 'date_joined',),
})


@admin.register(LibraryUser)
class LibraryUserAdmin(UserAdmin):

    form = LibraryUserChangeForm
    add_form = LibraryUserCreationForm
    list_display = (USERNAME_FIELD, 'email', 'banned')
    list_display_links = (USERNAME_FIELD,)
    list_filter = ('banned',)
    fieldsets = (
        BASE_FIELDS,
        SIMPLE_PERMISSION_FIELDS,
    )
    add_fieldsets = (
        (None, {
            'fields': REQUIRED_FIELDS + (
                'password1',
                'password2',
            ),
        }),
    )
    search_fields = (USERNAME_FIELD,)
    ordering = None
    filter_horizontal = tuple()
    readonly_fields = ('name', 'birth_year', 'city', 'sex')

admin.site.register(Book)