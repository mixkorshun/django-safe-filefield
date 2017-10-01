from django.conf import settings


def pytest_configure():
    settings.configure(
        SECRET_KEY='django-safe-filefield',

    )
