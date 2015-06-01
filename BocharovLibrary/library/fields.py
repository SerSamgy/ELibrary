from django import forms
from django.forms.widgets import TextInput
from django.core.validators import ValidationError

from constants import MIN_YEAR, MAX_YEAR


class YearField(forms.Field):
    widget = TextInput

    def clean(self, value):
        #First, run general validation (will catch, for example, a blank entry
        #if the field is required
        super(YearField, self).clean(value)

        try:
            value = int(value)
            if value < MIN_YEAR or value > MAX_YEAR:
                raise Exception()
            return value
        except:
            raise ValidationError('Invalid year.')