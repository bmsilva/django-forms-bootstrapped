__author__ = 'bms'

import logging

from django.test import TestCase

import django_forms_bootstrapped as forms
import django_forms_bootstrapped.widgets as widgets


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
        self.assertEqual(rendered, html, 'testing simple form with no bootstrap')

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
        self.assertEqual(rendered, html, 'testing simple form with bootstrap options')

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
        self.assertEqual(rendered, html, 'testing simple form_layout')

        SimpleForm.bootstrap_options['form_layout_sizes'] = (4, 6)
        sform = SimpleForm()
        rendered = sform.as_p()
        html = (
            u'<div class="form-group">'
            u'<label class="control-label col-sm-4" for="id_name">Name:</label> '
            u'<div class="col-sm-6">'
            u'<input class="form-control" id="id_name" maxlength="50" name="name" type="text" />'
            u'</div>'
            u'</div>'
        )
        self.assertEqual(rendered, html, 'Testing simple form_layout_sizes')


    def test_charfield(self):
        class SimpleForm(forms.Form):
            body = forms.CharField(widget=widgets.Textarea)

        sform = SimpleForm()
        rendered = sform.as_p()
        html = (
            u'<p class="form-group">'
            u'<label class="control-label" for="id_body">Body:</label> '
            u'<textarea class="form-control" cols="40" id="id_body" name="body" rows="10">\r\n</textarea>'
            u'</p>'
        )
        self.assertEqual(rendered, html)

    def test_choicefield(self):
        class SimpleForm(forms.Form):
            choose = forms.ChoiceField(
                choices=((1, 'choice 1'), (2, 'choice 2')))
            bootstrap_options = {}

        sform = SimpleForm()
        rendered = sform.as_p()
        html = (
            u'<p class="form-group">'
            u'<label class="control-label" for="id_choose">Choose:</label> '
            u'<select class="form-control" id="id_choose" name="choose">\n'
            u'<option value="1">choice 1</option>\n'
            u'<option value="2">choice 2</option>\n'
            u'</select>'
            u'</p>'
        )
        self.assertEqual(rendered, html)

        SimpleForm.bootstrap_options['as_p_use_divs'] = True
        sform = SimpleForm()
        rendered = sform.as_p()
        html = (
            u'<div class="form-group">'
            u'<label class="control-label" for="id_choose">Choose:</label> '
            u'<select class="form-control" id="id_choose" name="choose">\n'
            u'<option value="1">choice 1</option>\n'
            u'<option value="2">choice 2</option>\n'
            u'</select>'
            u'</div>'
        )
        self.assertEqual(rendered, html)

        SimpleForm.bootstrap_options['form_layout'] = 'form-horizontal'
        sform = SimpleForm()
        rendered = sform.as_p()
        html = (
            u'<div class="form-group">'
            u'<label class="control-label col-sm-2" for="id_choose">Choose:</label> '
            u'<div class="col-sm-10">'
            u'<select class="form-control" id="id_choose" name="choose">\n'
            u'<option value="1">choice 1</option>\n'
            u'<option value="2">choice 2</option>\n'
            u'</select>'
            u'</div>'
            u'</div>'
        )
        self.assertEqual(rendered, html)
