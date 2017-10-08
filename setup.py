from setuptools import find_packages, setup

setup(
    name='django-safe-filefield',
    version='0.2.0',
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
        'Environment :: Web Environment',
        'Framework :: Django',
        'Topic :: Security',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
