django-safe-filefield
=====================
.. image:: https://travis-ci.org/mixkorshun/django-safe-filefield.svg?branch=master
    :alt: build status
   :target: https://travis-ci.org/mixkorshun/django-safe-filefield
.. image:: https://codecov.io/gh/mixkorshun/django-safe-filefield/branch/master/graph/badge.svg
    :alt: code coverage
   :target: https://codecov.io/gh/mixkorshun/django-safe-filefield
.. image:: https://badge.fury.io/py/django-safe-filefield.svg
    :alt: pypi
   :target: https://pypi.python.org/pypi/django-safe-filefield
.. image:: https://img.shields.io/badge/code%20style-pep8-orange.svg
    :alt: pep8
   :target: https://www.python.org/dev/peps/pep-0008/
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT
   :target: https://opensource.org/licenses/MIT

Secure file field, which allows you to restrict uploaded file extensions.
It may be useful for user-uploaded files (attachments).

This package adds model and forms field. What this fields does:

 * restricts allowed file extensions (for example: only *.pdf files)
 * checks file extensions is correct for sent content-type
 * checks sent content type is correct for file content (detects by `libmagic`)
 * checks uploaded file with anti-virus software

Installation
------------

The package can be installed using:

.. code-block::

   pip install django-safe-filefield


Add the following settings:

.. code-block:: python

   INSTALLED_APPS += (
       'safe_filefield',
   )


**django-safe-filefield** require `libmagic` to be installed.

Usage
-----

Simply add field to your model:

.. code-block:: python

   from safe_filefield.models import SafeFileField

   class MyModel(models.Model):

       attachment = SafeFileField(
           allowed_extensions=('xls', 'xlsx', 'csv')
       )

Or to directly to your form:

.. code-block:: python

   from safe_filefield.forms import SafeFileField

   class MyForm(forms.Form):

       attachment = SafeFileField(
           allowed_extensions=('xls', 'xlsx', 'csv')
       )


ClamAV support
--------------

.. note:: To use this functionality you should have `clamd` daemon.

This package have ability to check uploaded file with ClamAV antivirus.

To use anti-virus protection simply enable it in your form or model definition:

.. code-block:: python

   from safe_filefield.forms import SafeFileField

   class MyForm(forms.Form):
       attachment = SafeFileField(
           scan_viruses=True,
       )


You can configure some ClamAV settings:

.. code-block:: python

   CLAMAV_SOCKET = 'unix://tmp/clamav.sock'  # or tcp://127.0.0.1:3310

   CLAMAV_TIMEOUT = 30  # 30 seconds timeout, by default None which means infinite


Contributing
------------

If you have any valuable contribution, suggestion or idea,
please let me know as well because I will look into it.

Pull requests are welcome.
