import mimetypes
import os

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

from . import clamav
from .utils import detect_content_type


@deconstructible
class FileExtensionValidator(object):
    message = _(
        "File extension '%(extension)s' is not allowed. "
        "Allowed extensions are: '%(allowed_extensions)s'."
    )
    code = 'invalid_extension'

    def __init__(self, allowed_extensions=None, message=None, code=None):
        self.allowed_extensions = allowed_extensions

        if message is not None:
            self.message = message

        if code is not None:
            self.code = code

    def __call__(self, value):
        extension = os.path.splitext(value.name)[1][1:].lower()

        if self.allowed_extensions is not None and extension not in self.allowed_extensions:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    'extension': extension,
                    'allowed_extensions': ', '.join(
                        self.allowed_extensions)
                }
            )


class FileContentTypeValidator:
    message = _(
        'File has invalid content-type. '
        'Maybe file extension is equal to file content?'
    )

    code = 'invalid_content_type'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message

        if code is not None:
            self.code = code

    def __call__(self, file):
        if hasattr(file, '_get_file'):
            file = file._get_file()

        __, ext = os.path.splitext(file.name)

        detected_content_type = detect_content_type(file)

        if getattr(file, 'content_type', None) is not None:
            is_valid_content_type = bool(
                (
                    ext in mimetypes.guess_all_extensions(detected_content_type)
                    and ext in mimetypes.guess_all_extensions(file.content_type)
                ) or (
                    detected_content_type == 'application/CDFV2-unknown'
                    and file.content_type == mimetypes.guess_type('.doc')
                    and ext == "doc"
                )
            )
            params={
                'extension': ext,
                'content_type': file.content_type,
                'detected_content_type': detected_content_type
            }
        else:
            is_valid_content_type = bool(
                (
                    ext in mimetypes.guess_all_extensions(detected_content_type)
                ) or (
                    detected_content_type == 'application/CDFV2-unknown'
                    and ext == "doc"
                )
            )
            params={
                'extension': ext,
                'content_type': None,
                'detected_content_type': detected_content_type
            }


        if not is_valid_content_type:
            raise ValidationError(
                self.message,
                code=self.code,
                params=params
            )


class AntiVirusValidator:
    message = _('File is infected with %(virus)s.')

    code = 'infected'

    def __init__(self, message=None, code=None):
        if message is not None:
            self.message = message

        if code is not None:
            self.code = code

    def __call__(self, file):
        status, virus_name = clamav.scan_file(file)

        if status != 'OK':
            raise ValidationError(
                self.message,
                self.code,
                params={
                    'virus': virus_name
                }
            )
