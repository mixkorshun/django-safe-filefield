from django.db import models

from . import forms
from .validators import FileContentTypeValidator, FileExtensionValidator


class SafeFileField(models.FileField):
    def __init__(self, **kwargs):
        self.allowed_extensions = kwargs.pop('allowed_extensions', None)
        self.check_content_type = kwargs.pop('check_content_type', True)

        default_validators = []

        if self.allowed_extensions:
            default_validators.append(
                FileExtensionValidator(self.allowed_extensions)
            )

        if self.check_content_type:
            default_validators.append(FileContentTypeValidator())

        self.default_validators = default_validators + self.default_validators

        super().__init__(**kwargs)

    def formfield(self, **kwargs):
        return super().formfield(
            form_class=forms.SafeFileField,

            allowed_extensions=self.allowed_extensions,
            check_content_type=self.check_content_type
        )
