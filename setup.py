import os
import sys
from setuptools import setup, Extension

from distutils.core import setup

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()



setup(
    name='NameProbability',
    version = '0.7.1',
    author = 'Zubin Jelveh',
    author_email='zj292@nyu.edu',
    packages=[''],
    data_files = [('data', ['data/ss_data.pkl', 'data/sample_names.csv'])],
    description = 'Name matching tool',
    install_requires=requirements,
    requires = [
        "Levenshtein",
        "NumPy",
    ],
)
