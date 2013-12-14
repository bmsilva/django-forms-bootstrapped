django-forms-bootstrapped
=========================

My Attempt to magically bootstrap django forms


Usage
-----

In your `app/forms.py`:

<pre>
from django.forms.models import modelform_factory, inlineformset_factory

from django_forms_bootstrapped import ModelForm

from app.models import City, Place

class PlaceForm(ModelForm):
    bootstrap_options = {
        'as_p_use_divs': True,
        'form_layout': 'form-horizontal',
    }

    class Meta:
        model = Place
        fields = [
            'name', 'gps_location', 'country',
        ]


CityForm = modelform_factory(City, form=ModelForm, fields=('name',))

PlaceFormSet = inlineformset_factory(City, Place, form=PlaceForm)
</pre>
