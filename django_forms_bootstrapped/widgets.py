import logging
from itertools import chain

import django.forms.widgets as widgets

from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


__all__ = (
    'TextInput', 'DateInput', 'CheckboxInput', 'Select', 'Textarea',
    'RadioSelect', 'DateTimeInput',
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


class ChoiceFieldRenderer(widgets.ChoiceFieldRenderer):
    def render(self):
        id_ = self.attrs.get('id', None)
        #start_tag = format_html('<ul id="{0}">', id_) if id_ else '<ul>'
        #output = [start_tag]
        output = []
        for widget in self:
            output.append(format_html('<div class="radio">{0}</div>', force_text(widget)))
        #output.append('</ul>')
        return mark_safe('\n'.join(output))


class ChoiceInput(widgets.ChoiceInput):
    pass


class RadioChoiceInput(ChoiceInput):
    pass


class RadioChoiceInput(widgets.RadioChoiceInput):
    pass


class RadioFieldRenderer(ChoiceFieldRenderer):
    choice_input_class = RadioChoiceInput


class RadioSelect(widgets.RadioSelect):
    renderer = RadioFieldRenderer


class DateTimeInput(widgets.DateTimeInput):
    def __init__(self, attrs=None):
        super(DateTimeInput, self).__init__(add_class(attrs, 'form-control'))
