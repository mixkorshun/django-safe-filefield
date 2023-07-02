from setuptools import find_packages, setup

setup(
    name='django-safe-filefield',
    version='0.3.1',
    url='https://github.com/mixkorshun/django-safe-filefield',
    description='Secure file field, which allows you to '
                'restrict uploaded file extensions.',
    keywords=['django', 'filefield', 'model-field', 'form-field'],

    long_description=open('README.rst', 'r').read(),

    author='Vladislav Bakin',
    author_email='mixkorshun@gmail.com',
    maintainer='Vladislav Bakin',
    maintainer_email='mixkorshun@gmail.com',

    license='MIT',

    install_requires=[
        'django',

        'python-magic',
        'clamd',
    ],

    packages=find_packages(exclude=['*.tests.*', '*.tests']),

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4',
        'Framework :: Django :: 4.2',
    ],
)
