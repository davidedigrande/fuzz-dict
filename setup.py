from setuptools import setup, find_packages

NAME = "fuzdict"
VERSION = '0.0.1' 
DESCRIPTION = 'A Python dictionary with fuzzy-matched keys.'
LONG_DESCRIPTION = \
"""
FuzDict is a simple python dictionary that implements Fuzzy Logic as a way to match keys.
This implies that suitable values for creating keys are only of string type.
It also implies that at any time, the dictionary cannot have two or more similar strings, which means in turn that the input order matters.
"""
AUTHOR="Davide Di Grande"
EMAIL = "davidedigrande94@gmail.com"

setup(
        name=NAME, 
        version=VERSION,
        author=AUTHOR,
        author_email=EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["fuzzywuzzy==0.18.0"],         
        keywords=['python'],
)