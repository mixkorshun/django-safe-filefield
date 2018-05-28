import pytest
from django.core.exceptions import ValidationError

from .utils import get_extras_file, get_uploaded_file
from .. import forms
from ..models import SafeFileField


class TestSafeFormField:
    def test_valid_file(self):
        field = SafeFileField(allowed_extensions=('jpg',))

        f = get_uploaded_file(get_extras_file('sample.jpg'))

        field.clean(f, None)

        assert True

    def test_not_allowed_extension(self):
        field = SafeFileField(allowed_extensions=('png',))

        f = get_uploaded_file(get_extras_file('sample.jpg'))

        with pytest.raises(ValidationError):
            field.clean(f, None)

    def test_invalid_content_type(self):
        field = SafeFileField(allowed_extensions=('jpg',))

        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type='image/png')

        with pytest.raises(ValidationError):
            field.clean(f, None)

    def test_invalid_content_type2(self):
        field = SafeFileField(allowed_extensions=('png',))

        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type='image/png',
                              upload_name='sample.png')

        with pytest.raises(ValidationError):
            field.clean(f, None)

    def test_formfield(self):
        field = SafeFileField(allowed_extensions=('.jpg',))

        form_field = field.formfield()

        assert isinstance(form_field, forms.SafeFileField)
        assert form_field.allowed_extensions == ('.jpg',)
