from itertools import chain

import django.forms.widgets as widgets


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

    def render(self, name, value, attrs=None):
        attrs['placeholder'] = name
        return super(TextInput, self).render(name, value, attrs)


class DateInput(widgets.DateInput):
    def __init__(self, attrs=None):
        super(DateInput, self).__init__(add_class(attrs, 'form-control'))

    def render(self, name, value, attrs=None):
        attrs['placeholder'] = name
        return super(DateInput, self).render(name, value, attrs)


class CheckboxInput(widgets.CheckboxInput):
    pass
