import mimetypes
import os

from django.core.files.uploadedfile import UploadedFile

extras_dir = os.path.join(os.path.dirname(__file__), 'extras')
mimetypes.init()


def get_extras_file(name):
    return os.path.join(extras_dir, name)


def get_uploaded_file(filename, content_type=None, upload_name=None):
    if content_type is False:
        return UploadedFile(open(filename, 'rb'),
                            upload_name or os.path.basename(filename), None)
    return UploadedFile(
        open(filename, 'rb'),
        upload_name or os.path.basename(filename),
        content_type or mimetypes.guess_type(filename)[0]
    )
