import os
from setuptools import setup, find_packages

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/README.md') as f:
    description = f.read()

setup(
    name='wallymart',
    description='UCSC OOAD Class, Project X, built on django',
    long_description=description,
    version='1.0',
    author='Harrison Wang',
    author_email='harrison.c.wang@gmail.com',
    # packages=find_packages(exclude=['tests']),
    include_package_data=True,
)
