import pytest
from django.core.exceptions import ValidationError

from .utils import get_extras_file, get_uploaded_file
from ..validators import FileContentTypeValidator, FileExtensionValidator


class TestFileExtensionValidator:
    cls = FileExtensionValidator

    def test_allowed_extension(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'))

        validator = FileExtensionValidator(('jpg',))

        validator(f)

    def test_disallowed_extension(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'))

        validator = FileExtensionValidator(('png',))

        with pytest.raises(ValidationError):
            validator(f)


class TestFileContentTypeValidator:
    def test_correct_content_type(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'))

        validator = FileContentTypeValidator()

        validator(f)

    def test_incorrect_content_type(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type='image/png')

        validator = FileContentTypeValidator()

        with pytest.raises(ValidationError):
            validator(f)
