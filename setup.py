from setuptools import find_packages, setup

setup(
    name='django-safe-filefield',
    version='0.1.1',
    url='https://github.com/mixkorshun/django-safe-filefield',
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
    ],

    packages=find_packages(exclude=['*.tests.*', '*.tests']),

    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
