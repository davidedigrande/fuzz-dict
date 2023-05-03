from pathlib import Path

from pip._internal.req import parse_requirements
from setuptools import find_packages, setup

setup(
    name="fuzz-dict",
    version="0.0.4",
    author="Davide Di Grande",
    author_email="davidedigrande.dev@gmail.com",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[ir.requirement for ir in parse_requirements("requirements.txt", session=False)],
    project_urls={"Source": "https://github.com/davidedigrande/fuzz-dict"},
)
