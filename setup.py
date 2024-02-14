from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='selenium_auto_executor',
    version='1.0.3',
    description='selenium_auto_executor',
    author='XB605324585',
    author_email='XB605324585@gmail.com',
    packages=find_packages(),
    python_requires='>=3.8.7',
    install_requires=requirements,
)
