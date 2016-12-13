try:
    from django.forms.util import ErrorList
except ImportError:
    from django.forms.utils import ErrorList
from django.utils.html import format_html_join
from django.utils.encoding import force_text


class ErrorList(ErrorList):
    """
    A collection of errors that knows how to display itself in various formats.
    """
    def __str__(self):
        return self.as_p()

    def as_p(self):
        if not self: return ''
        return format_html_join('', '<p class="text-danger">{0}</p>',
            ((force_text(e),) for e in self)
        )
