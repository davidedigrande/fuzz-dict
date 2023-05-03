from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

setup(
    name="fuzz-dict", 
    version="0.0.1" ,
    author="Davide Di Grande",
    author_email="davidedigrande.dev@gmail.com",
    packages=find_packages(),
    install_requires=[ir.requirement for ir in parse_requirements('requirements.txt', session=False)],
)