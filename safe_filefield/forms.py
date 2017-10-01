from django import forms
from django.core.exceptions import ValidationError

from .validators import default_error_messages, has_allowed_extension, \
    has_correct_content_type


class SafeFileField(forms.FileField):
    default_error_messages = default_error_messages

    def __init__(self, **kwargs):
        self.allowed_extensions = kwargs.pop('allowed_extensions', None)
        self.strict_content_type = kwargs.pop('strict_content_type', True)

        super().__init__(**kwargs)

    def validate(self, value):
        super().validate(value)

        if not value:
            return

        if self.allowed_extensions \
                and not has_allowed_extension(value, self.allowed_extensions):
            _msg = self.error_messages['file_type'] % {
                'types': ', '.join(self.allowed_extensions)
            }
            raise ValidationError(_msg, code='file_type')

        if not has_correct_content_type(value, self.strict_content_type):
            raise ValidationError(
                self.error_messages['file_content_type'],
                code='file_content_type'
            )
