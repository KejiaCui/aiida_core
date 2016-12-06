# -*- coding: utf-8 -*-
import os

__copyright__ = u"Copyright (c), This file is part of the AiiDA platform. For further information please visit http://www.aiida.net/. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file."
__version__ = "0.7.0"
__authors__ = "The AiiDA team."

from setuptools import setup, find_packages

# Get the version number
aiida_folder = os.path.split(os.path.abspath(__file__))[0]
fname = os.path.join(aiida_folder, 'aiida', '__init__.py')
with open(fname) as aiida_init:
    ns = {}
    exec (aiida_init.read(), ns)
    aiida_version = ns['__version__']

bin_folder = os.path.join(aiida_folder, 'bin')
setup(
    name='aiida',
    url='http://www.aiida.net/',
    license='MIT license, see LICENSE.txt',
    version=aiida_version,
    # Abstract dependencies.  Concrete versions are listed in
    # requirements.txt
    # See https://caremad.io/2013/07/setup-vs-requirement/ for an explanation
    # of the difference and
    # http://blog.miguelgrinberg.com/post/the-package-dependency-blues
    # for a useful dicussion
    install_requires=[
        'django==1.7.4',
        'django_extensions==1.5',
        'pytz==2014.10',
        'django-celery==3.1.16',
        'celery==3.1.17',
        'billiard==3.3.0.19',
        'anyjson==0.3.3',
        'six==1.9',
        'supervisor==3.1.3',
        'meld3==1.0.0',
        'numpy',
        'plum==0.4.3'
        'SQLAlchemy==1.0.12',
        'SQLAlchemy-Utils==0.31.2',
        'ujson==1.35',
        'enum34==1.1.2',
        'voluptuous==0.8.11',
        'aldjemy',
        'passlib',
        'validate_email',
        'click==6.6',
        'tabulate==0.7.5',
        'ete3==3.0.0b35',
    ],
    extra_require={
        'verdi_shell': ['ipython'],
        'ssh': [
            'paramiko==1.15.2',
            'ecdsa==0.13',
            'pycrypto==2.6.1',
        ],
        'REST': [
            'django-tastypie==0.12.1',
            'python-dateutil==2.4.0',
            'python-mimeparse==0.1.4',
        ],
    },
    dependency_links=[
        'git+https://bitbucket.org/aiida_team/plum.git@v0.4.3#egg=plum',
    ],
    packages=find_packages(),
    scripts=[os.path.join(bin_folder, f) for f in os.listdir(bin_folder)
             if not os.path.isdir(os.path.join(bin_folder, f))],
    long_description=open(os.path.join(aiida_folder, 'README.rst')).read(),
)
