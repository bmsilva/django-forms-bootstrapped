from itertools import chain

import logging

from django.forms.fields import BooleanField as DJBooleanField

import django.forms.forms as fforms

from .util import ErrorList
from .fields import CharField, DateField, BooleanField


log = logging.getLogger(__name__)


class BoundField(fforms.BoundField):
    def css_classes(self, extra_classes=None):
        ec = extra_classes or []

        opts = getattr(self.field, 'bootstrap_options', {})
        if 'extra_classes' in opts:
            ec.extend(opts['extra_classes'])

        if self.errors:
            ec.append("has-error")
        return super(BoundField, self).css_classes(extra_classes=ec)

    def label_tag(self, contents=None, attrs=None, label_suffix=None):
        opts = getattr(self.field, 'bootstrap_options', {})

        classes = []
        if self.form.bootstrap_opts['form_layout'] == 'form-horizontal':
            classes.append('col-sm-{}'.format(
                self.form.bootstrap_opts['form_layout_sizes'][0],
            ))

        label_classes = opts.get('label_classes', [])
        if (len(label_classes) + len(classes)) == 0:
            attrs = dict(attrs or {})
        else:
            classes_joined = {
                'class': ' '.join(chain(label_classes, classes))
            }
            attrs = dict( attrs or {}, **classes_joined )
        return super(BoundField, self).label_tag(contents, attrs, label_suffix)

    def __str__(self):
        """Renders this field as an HTML widget."""
        attrs = None
        if getattr(self.field, 'placeholder', None) is not None:
            if callable(self.field.placeholder):
                attrs = {'placeholder': self.field.placeholder()}
            else:
                attrs = {'placeholder': self.field.placeholder}
        if self.field.show_hidden_initial:
            return self.as_widget(attrs=attrs) + self.as_hidden(
                only_initial=True)
        return self.as_widget(attrs=attrs)


class Form(fforms.Form):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False):
        super(Form, self).__init__(
            data, files, auto_id, prefix, initial, error_class, label_suffix,
            empty_permitted
        )

    @property
    def bootstrap_opts(self):
        return dict({
                        'form_layout': '',
                        'form_layout_sizes': (2, 10),
                        'as_p_use_divs': False,
                    }, **getattr(self, 'bootstrap_options', {}))

    def __getitem__(self, name):
        "Returns a BoundField with the given name."

        try:
            field = self.fields[name]
        except KeyError:
            raise KeyError('Key %r not found in Form' % name)

        "Fixing delete field from formset"
        if name == 'DELETE' and isinstance(field, DJBooleanField):
            field = BooleanField(label=field.label, required=field.required)
            self.fields[name] = field

        return BoundField(self, field, name)

    def as_p(self):
        field_str = '%(field)s'
        if self.bootstrap_opts['form_layout'] == 'form-horizontal':
            field_str = '<div class="col-sm-{size}">{field}</div>'.format(
                size=self.bootstrap_opts['form_layout_sizes'][1],
                field=field_str,
            )
        if self.bootstrap_opts['as_p_use_divs']:
            normal_row = (
                '<div%(html_class_attr)s>'
                '%(label)s {field}%(help_text)s'
                '</div>'
            ).format(field=field_str)
            row_ender = '</div>'
        else:
            normal_row = (
                '<p%(html_class_attr)s>'
                '%(label)s {field}%(help_text)s'
                '</p>'
            ).format(field=field_str)
            row_ender = '</p>'
        return self._html_output(
            normal_row=normal_row,
            error_row='%s',
            row_ender=row_ender,
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)
