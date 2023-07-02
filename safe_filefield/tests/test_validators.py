import os
from unittest.mock import Mock

import clamd
import pytest
from django.core.exceptions import ValidationError
from django.test import override_settings

from safe_filefield import clamav
from .utils import get_extras_file, get_uploaded_file
from ..validators import AntiVirusValidator, FileContentTypeValidator, \
    FileExtensionValidator


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

    def test_no_content_type(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type=False)

        validator = FileContentTypeValidator()

        validator(f)

    def test_incorrect_content_type(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type='image/png')

        validator = FileContentTypeValidator()

        with pytest.raises(ValidationError):
            validator(f)

    def test_incorrect_content_type2(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type='image/png',
                              upload_name='sample.png')

        validator = FileContentTypeValidator()

        with pytest.raises(ValidationError):
            validator(f)

    def test_incorrect_content_type3(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              upload_name='sample.png')

        validator = FileContentTypeValidator()

        with pytest.raises(ValidationError):
            validator(f)

    def test_no_content_type_with_bad_ext(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'),
                              content_type=False,
                              upload_name='sample.png')

        validator = FileContentTypeValidator()

        with pytest.raises(ValidationError):
            validator(f)

    def test_not_uploadedfile_instance(self):
        f = get_uploaded_file(get_extras_file('sample.jpg'))
        m = Mock()
        m._get_file = lambda: f

        validator = FileContentTypeValidator()

        validator(m)


CLAMAV_SOCKET = os.environ.get('CLAMAV_SOCKET', 'unix:///tmp/clamd.sock')


class TestAntiVirusValidator:
    @override_settings(
        CLAMAV_SOCKET=CLAMAV_SOCKET
    )
    def test_infected_file(self):
        try:
            clamav.scanner.ping()
        except clamd.ConnectionError:
            pytest.skip('Is `clamd` daemon running?')

        f = get_uploaded_file(get_extras_file('infected.dat'))

        validator = AntiVirusValidator()

        with pytest.raises(ValidationError):
            validator(f)

    @override_settings(
        CLAMAV_SOCKET=CLAMAV_SOCKET
    )
    def test_normal_file(self):
        try:
            clamav.scanner.ping()
        except clamd.ConnectionError:
            pytest.skip('Is `clamd` daemon running?')

        f = get_uploaded_file(get_extras_file('sample.jpg'))

        validator = AntiVirusValidator()

        validator(f)
