# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='WsgiUnproxy',
    version='1.0',
    description='Unproxy WSGI middleware',
    author='Søren Løvborg',
    author_email='kwi@kwi.dk',
    url='https://bitbucket.org/kwi/wsgiunproxy/',
    license='Public Domain',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
    ],

    long_description=open('README.txt', 'r').read(),
    packages=['wsgiunproxy'],
    zip_safe=True,
    entry_points = {
        'paste.filter_factory': [
            'main=wsgiunproxy:paste_filter_factory',
        ]
    },
)
