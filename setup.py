#!/usr/bin/python

from setuptools import setup, find_packages

class post_install():
    def run(self):
        os.system('glib-compile-schemas /usr/share/glib-2.0/schemas')
        os.system('sudo gtk-update-icon-cache -f -t /usr/share/icons/hicolor/')


my_data_files = [
    ('/usr/share/icons/hicolor/scalable/apps/', ['boilerplate/data/icons/scalable/boilerplate.svg']),
    ('/usr/share/icons/hicolor/16x16/apps/', ['boilerplate/data/icons/16x16/boilerplate-16.png']),
    ('/usr/share/icons/hicolor/24x24/apps/', ['boilerplate/data/icons/24x24/boilerplate-24.png']),
    ('/usr/share/icons/hicolor/32x32/apps/', ['boilerplate/data/icons/32x32/boilerplate-32.png']),
    ('/usr/share/icons/hicolor/48x48/apps/', ['boilerplate/data/icons/48x48/boilerplate-48.png']),
    ('/usr/share/icons/hicolor/64x64/apps/', ['boilerplate/data/icons/64x64/boilerplate-64.png']),
    ('/usr/share/applications/', ['boilerplate.desktop']),
    ('/usr/share/glib-2.0/schemas/', ['boilerplate.gschema.xml']),
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
