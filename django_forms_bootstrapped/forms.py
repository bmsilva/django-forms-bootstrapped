from itertools import chain

import logging

import django.forms.forms as fforms


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

        attrs = dict(
            attrs or {},
            **{'class': ' '.join(chain(opts['label_classes'], classes))}
        )
        return super(BoundField, self).label_tag(contents, attrs, label_suffix)
