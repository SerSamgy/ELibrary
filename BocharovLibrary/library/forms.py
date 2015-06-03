from django import forms
from django.apps import apps as django_apps
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import StrictButton

from fields import YearField


User = get_user_model()
# get model after application had been registered
app = django_apps.get_app_config('library')
Genre = app.get_model('Genre')

class LibraryUserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above,"
                                            " for verification."))

    class Meta:
        model = User
        fields = (User.USERNAME_FIELD,) + \
                 tuple(User.REQUIRED_FIELDS)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch']
            )
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(LibraryUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LibraryUserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class BookSearchForm(forms.Form):
    author = forms.CharField(label=_("Автор"), max_length=64, required=False)
    title = forms.CharField(label=_("Название"), max_length=255, required=False)
    genre = forms.ModelChoiceField(Genre.objects.all(), label=_("Жанр"),
                                   required=False)
    year = YearField(label=_("Год издания"), required=False)
    publisher = forms.CharField(label=_("Издательство"), max_length=64,
                                required=False)

    def __init__(self, *args, **kwargs):
        super(BookSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-lg-2"
        self.helper.field_class = "col-lg-10"
        self.helper.layout = Layout(
            'author',
            'title',
            'genre',
            'year',
            'publisher',
            StrictButton(_("Поиск"), type='submit',
                         css_class="btn-primary btn-hg"),
            StrictButton(_("Очистить"), css_class="btn-default")
        )