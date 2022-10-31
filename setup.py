#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='bukut', 
        version='0.13', 
        description='Bookmarks manager', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/bukut',
        scripts=['bukut'],
        install_requires=['asciimatics', 'beautifulsoup4', 'natsort', 'pyperclip', 'tuicolor @ git+https://github.com/peterjschroeder/tuicolor.git']
)

