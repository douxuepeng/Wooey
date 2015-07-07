import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wooey',
    version='0.2.6',
    packages=find_packages(),
    scripts=['scripts/wooify'],
    entry_points={'console_scripts': ['wooify = wooey.backend.command_line:bootstrap',]},
    install_requires = ['Django>=1.6', 'django-autoslug', 'django-celery', 'six'],
    include_package_data=True,
    license='GPLv3',
    description='A Django app which creates a web GUI and task interface for argparse scripts',
    url='http://www.github.com/wooey/django-djangui',
    author='Chris Mitchell',
    author_email='chris.mit7@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

