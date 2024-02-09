from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='selenium_auto_executor',
    version='1.0.2',
    description='selenium_auto_executor',
    author='XB605324585',
    author_email='XB605324585@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
)
