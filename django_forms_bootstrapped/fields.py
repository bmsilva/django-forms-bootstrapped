import django.forms.fields as djfields

from .widgets import TextInput, DateInput, CheckboxInput


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


class BooleanField(djfields.BooleanField):
    widget = CheckboxInput
    bootstrap_options = {
        'extra_classes': ["form-group"],
        'label_classes': ["control-label"],
    }
