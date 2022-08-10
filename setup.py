from setuptools import setup, find_packages
from codecs import open
from os import path
import io
import re


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


with io.open("ploto_sokort/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='ploto_sokort',

    version=version,

    description='A plugin for ploto to use sokort',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/nwpc-oper/ploto-sokort',

    author='perillaroc',
    author_email='perillaroc@gmail.com',

    license='Apache License, Version 2.0',

    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),

    include_package_data=True,

    package_data={
        '': ['*.ncl'],
    },

    zip_safe=False,

    install_requires=[
    ],
)
