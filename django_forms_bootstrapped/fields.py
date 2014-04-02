import django.forms.fields as djfields

from .widgets import (
    TextInput, DateInput, CheckboxInput, Select, DateTimeInput,
)

__all__ = (
    'CharField', 'DateField', 'BooleanField', 'ChoiceField', 'DateTimeField',
)


class CharField(djfields.CharField):
    widget = TextInput
    bootstrap_options = {
        'extra_classes': ["form-group"],
        'label_classes': ["control-label"],
    }


class DateField(djfields.DateField):
    widget = DateInput
    bootstrap_options = {
        'extra_classes': ["form-group"],
        'label_classes': ["control-label"],
    }

    def __init__(self, *args, **kwargs):
        self.placeholder = kwargs.pop('placeholder', None)
        return super(DateField, self).__init__(*args, **kwargs)


class BooleanField(djfields.BooleanField):
    widget = CheckboxInput
    bootstrap_options = {
        'extra_classes': ["form-group"],
        'label_classes': ["control-label"],
    }


class ChoiceField(djfields.ChoiceField):
    widget = Select
    bootstrap_options = {
        'extra_classes': ["form-group"],
        'label_classes': ["control-label"],
    }


class DateTimeField(djfields.DateTimeField):
    widget = DateTimeInput
    bootstrap_options = {
        'extra_classes': ["form-group"],
        'label_classes': ["control-label"],
        }

    def __init__(self, *args, **kwargs):
        self.placeholder = kwargs.pop('placeholder', None)
        return super(DateTimeField, self).__init__(*args, **kwargs)
