import logging
from itertools import chain

import django.forms.widgets as widgets


__all__ = (
    'TextInput', 'DateInput', 'CheckboxInput', 'Select', 'Textarea',
)


log = logging.getLogger('__name__')


def add_class(attrs, *args):
    battrs = dict(attrs or {})
    if 'class' in battrs:
        classes = chain(battrs['class'], args)
    else:
        classes = args
    battrs['class'] = ' '.join(classes)
    return battrs


class TextInput(widgets.TextInput):
    def __init__(self, attrs=None):
        super(TextInput, self).__init__(add_class(attrs, 'form-control'))


class DateInput(widgets.DateInput):
    def __init__(self, attrs=None):
        super(DateInput, self).__init__(add_class(attrs, 'form-control'))


class CheckboxInput(widgets.CheckboxInput):
    pass


class Select(widgets.Select):
    def __init__(self, attrs=None):
        super(Select, self).__init__(add_class(attrs, 'form-control'))


class Textarea(widgets.Textarea):
    def __init__(self, attrs=None):
        super(Textarea, self).__init__(add_class(attrs, 'form-control'))
