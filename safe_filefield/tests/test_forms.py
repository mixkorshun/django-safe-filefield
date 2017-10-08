import pytest
from django.core.exceptions import ValidationError

from .utils import get_extras_file, get_uploaded_file
from ..forms import SafeFileField


class TestSafeFileField:
    def test_valid_file(self):
        field = SafeFileField(allowed_extensions=('jpg',),
                              allow_empty_file=True)

        f = get_uploaded_file(get_extras_file('sample.jpg'))

        field.clean(f)

        assert True

    def test_not_allowed_extension(self):
        field = SafeFileField(allowed_extensions=('png',),
                              allow_empty_file=True)

        f = get_uploaded_file(get_extras_file('sample.jpg'))

        with pytest.raises(ValidationError) as err_info:
            field.clean(f)

        assert err_info.value.error_list[0].code == 'invalid_extension'

    def test_invalid_content_type(self):
        field = SafeFileField(allowed_extensions=('jpg',),
                              allow_empty_file=True)

        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type='image/png')

        with pytest.raises(ValidationError) as err_info:
            field.clean(f)

        assert err_info.value.error_list[0].code == 'invalid_content_type'
