#!/usr/bin/python

from setuptools import setup, find_packages

my_data_files = [
    ('/usr/share/applications/', ['boilerplate.desktop']),
    ('/usr/share/glib-2.0/schemas/', ['apps.boilerplate.gschema.xml']),
    ]

setup(
    name = "boilerplate",
    version = "0.2",
    author = "Ryan Lerch",
    author_email = "rlerch@redhat.com",
    description = "a python gtk boilerplate",
    license = "GPL2",
    keywords = "sample",
    url = "ryanlerch.org",

    scripts = ['boilerplate/boilerplate'],
    data_files = my_data_files,
    packages = find_packages(),
)
