from django.core.exceptions import ValidationError
from django.db import models

from . import forms
from .validators import default_error_messages, has_allowed_extension, \
    has_correct_content_type


class SafeFileField(models.FileField):
    default_error_messages = default_error_messages

    def __init__(self, **kwargs):
        self.allowed_extensions = kwargs.pop('allowed_extensions', None)
        self.strict_content_type = kwargs.pop('strict_content_type', True)

        super().__init__(**kwargs)

    def formfield(self, **kwargs):
        return super().formfield(
            form_class=forms.SafeFileField,

            allowed_extensions=self.allowed_extensions,
            strict_content_type=self.strict_content_type
        )

    def validate(self, value, model_instance):
        super().validate(value, model_instance)

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
