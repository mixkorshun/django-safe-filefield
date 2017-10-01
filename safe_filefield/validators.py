import mimetypes
import os

from django.utils.translation import ugettext_lazy as _

from .utils import detect_content_type

default_error_messages = {
    'file_type': _('Sent file type is not allowed. '
                   'Allowed file types: %(types)s'),

    'file_content_type': _('Wrong file content type. '
                           'Check your file extension.'),
}


def has_allowed_extension(f, allowed_extensions):
    __, ext = os.path.splitext(f.name)

    return ext in allowed_extensions


def has_correct_content_type(f, strict=True):
    __, ext = os.path.splitext(f.name)

    if ext not in mimetypes.guess_all_extensions(f.content_type):
        return False

    if strict:
        detected_content_type = detect_content_type(f)

        return bool(
            (
                detected_content_type == 'application/CDFV2-unknown'
                and f.content_type == mimetypes.guess_type('.doc')
            ) or (
                detected_content_type == f.content_type
            )
        )
    else:
        return True
