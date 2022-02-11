from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A Python dictionary with fuzzy-matched keys.'
LONG_DESCRIPTION = 'A Python dictionary with fuzzy-matched keys.'

with open('requirements.txt') as requirements:
    requirements = requirements.readlines()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="fuzzydict", 
        version=VERSION,
        author="Davide Di Grande",
        author_email="davidedigrande94@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=requirements,         
        keywords=['python'],
)