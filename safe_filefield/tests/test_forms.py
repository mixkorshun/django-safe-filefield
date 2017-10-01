import pytest
from django.core.exceptions import ValidationError

from .utils import get_extras_file, get_uploaded_file
from ..forms import SafeFileField


class TestSafeFileField:
    def test_valid_file(self):
        field = SafeFileField(allowed_extensions=('.jpg',))

        f = get_uploaded_file(get_extras_file('sample.jpg'))

        field.validate(f)

        assert True

    def test_not_allowed_extension(self):
        field = SafeFileField(allowed_extensions=('.png',))

        f = get_uploaded_file(get_extras_file('sample.jpg'))

        with pytest.raises(ValidationError):
            field.validate(f)

    def test_invalid_content_type(self):
        field = SafeFileField(allowed_extensions=('.jpg',))

        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type='image/png')

        with pytest.raises(ValidationError):
            field.validate(f)
