__author__ = 'bms'

import logging

from django.test import TestCase

import django_forms_bootstrapped.forms as forms


log = logging.getLogger(__name__)


class FormTestCase(TestCase):
    def setUp(self):
        pass

    def test_simple_form(self):
        class SimpleForm(forms.Form):
            name = forms.CharField(max_length=50)

        sform = SimpleForm()
        rendered = sform.as_p()
        html = (
            u'<p class="form-group">'
            u'<label class="control-label" for="id_name">Name:</label> '
            u'<input class="form-control" id="id_name" maxlength="50" name="name" type="text" />'
            u'</p>'
        )
        self.assertEqual(rendered, html)

    def test_simple_form_bootstrap_options(self):
        class SimpleForm(forms.Form):
            name = forms.CharField(max_length=50)
            bootstrap_options = {
                'as_p_use_divs': True,
            }

        sform = SimpleForm()
        rendered = sform.as_p()
        html = (
            u'<div class="form-group">'
            u'<label class="control-label" for="id_name">Name:</label> '
            u'<input class="form-control" id="id_name" maxlength="50" name="name" type="text" />'
            u'</div>'
        )
        self.assertEqual(rendered, html)

        SimpleForm.bootstrap_options['form_layout'] = 'form-horizontal'
        sform = SimpleForm()
        rendered = sform.as_p()
        html = (
            u'<div class="form-group">'
            u'<label class="control-label col-sm-2" for="id_name">Name:</label> '
            u'<div class="col-sm-10">'
            u'<input class="form-control" id="id_name" maxlength="50" name="name" type="text" />'
            u'</div>'
            u'</div>'
        )
        self.assertEqual(rendered, html)


