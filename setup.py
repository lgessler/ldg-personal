#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", 'r', encoding='utf-8') as f:
    desc = f.read()

setup(
    name="ldg",
    description="Luke's personal Python snippet library",
    long_description=desc,
    long_description_content_type="text/markdown",
    author="Luke Gessler",
    author_email="lukegessler@gmail.com",
    url="https://github.com/lgessler/ldg-personal",
    packages=find_packages(),
    include_package_data=True,
    version="0.0.1",
    install_requires=[
    ],
    dependency_links=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6"
    ]
)

