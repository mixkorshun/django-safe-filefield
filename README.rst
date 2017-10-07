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

Allow you easily check file for extension by content-type
and detected by content content-type. Useful to user-uploaded files.

This package add model and forms field. What this fields do:
 * restrict allowed file extensions (for example: only *.pdf files)
 * checks file extension is correct for sent content-type
 * checks sent content type is correct for file content (detect by libmagic)

Installation
------------

The package can be installed using:

.. code-block::

   pip install django-parler


Add the following settings:

.. code-block:: python

   INSTALLED_APPS += (
       'safe_filefield',
   )


.. note:: **django-safe-filefield** require `libmagic` to be installed.

Usage
-----

Simply add field to your model:

.. code-block:: python

   from safe_filefield.models import SafeFileField

   class MyModel(models.Model):

       attachment = SafeFileField(
           allowed_extensions=('.xls', '.xlsx', '.csv')
       )

Or to directly to your form:

.. code-block:: python

   from safe_filefield.forms import SafeFileField

   class MyForm(forms.Model):

       attachment = SafeFileField(
           allowed_extensions=('.xls', '.xlsx', '.csv')
       )


Contributing
------------

If you have any valuable contribution, suggestion or idea,
please let me know as well because I will look into it.

Pull requests are welcome.
