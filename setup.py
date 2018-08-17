"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2018 RedFantom
"""
from setuptools import setup


def read(file_name):
    """Return the contents of a given file"""
    with open(file_name) as fi:
        return fi.read()


setup(
    name="tkextrafont",
    packages=["tkextrafont"],
    package_data={"tkextrafont": ["*.tcl", "*.so", "*.dll", "*/*"]},
    version="0.0.1",
    description="A Python wrapper to load the Tcl library extrafont into a Tk interpreter",
    author="RedFantom",
    author_email="redfantom@outlook.com",
    url="https://github.com/RedFantom/python-tkextrafont",
    include_package_data=True,
    zip_safe=False,
    keywords=["tkinter", "gui", "tcl"],
    license="GPLv3",
    long_description=read("README.md"),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Tcl Extensions',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
