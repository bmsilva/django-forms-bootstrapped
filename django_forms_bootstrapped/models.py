import logging

from django.db import models
from django.forms.models import ModelFormMetaclass as MFM, ModelForm as MF
from django.forms.fields import BooleanField as DJBooleanField
from django.utils import six

from .forms import BoundField
from .fields import CharField, DateField, BooleanField
from .util import ErrorList


log = logging.getLogger(__name__)
__all__ = ('ModelForm', )


def bootstrap_formfield_callback(f, **kwargs):
    if isinstance(f, models.CharField):
        kwargs['form_class'] = CharField
    elif isinstance(f, models.DateField):
        kwargs['form_class'] = DateField
    elif isinstance(f, models.BooleanField):
        kwargs['form_class'] = BooleanField
    return f.formfield(**kwargs)


class ModelFormMetaclass(MFM):
    def __new__(cls, name, bases, attrs):
        attrs['formfield_callback'] = bootstrap_formfield_callback
        return super(ModelFormMetaclass, cls).__new__(cls, name, bases, attrs)


class ModelForm(six.with_metaclass(ModelFormMetaclass, MF)):

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, instance=None,
                 use_required_attribute=None):
        super(ModelForm, self).__init__(
            data, files, auto_id, prefix, initial, error_class, label_suffix,
            empty_permitted, instance, use_required_attribute,
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
            normal_row = '<div%(html_class_attr)s>%(label)s {field}%(help_text)s</div>'.format(  # noqa
                field=field_str,
            )
            row_ender = '</div>'
        else:
            normal_row = '<p%(html_class_attr)s>%(label)s {field}%(help_text)s</p>'.format(  # noqa
                field=field_str,
            )
            row_ender = '</p>'
        return self._html_output(
            normal_row=normal_row,
            error_row='%s',
            row_ender=row_ender,
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)
