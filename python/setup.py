import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = read("requirements.txt").split()

setup(
    name="arkhn-monitoring",
    version="0.0.4",
    author="Arkhn",
    author_email="contact@arkhn.org",
    description="Helper functions used to monitor Arkhn's stack.",
    url="https://github.com/arkhn/monitoring",
    license="Apache License 2.0",
    packages=find_packages(),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=requirements,
)
