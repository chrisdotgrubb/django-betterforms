#!/usr/bin/env python
from setuptools import setup, find_packages
import os

__doc__ = """
App for Django featuring improved form base classes.
Forked from better-forms, then updated for python3 and django 4.0
"""

version = '2.0.0'


def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
	name='django-betterforms',
	version=version,
	description=__doc__,
	long_description=read('README.rst'),
	url="https://github.com/chrisdotgrubb/django-betterforms",
	author="grubb",
	author_email='developer.grubb@gmail.com',
	packages=[package for package in find_packages()
			  if package.startswith('betterforms')],
	install_requires=['Django>=3.0'],
	zip_safe=False,
	include_package_data=True,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Framework :: Django :: 4.0',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Topic :: Internet :: WWW/HTTP',
	],
)
