"""setup.py for ventplotting package."""
import setuptools


PACKAGE_NAME = 'ventplotting'


# MAIN SETUP

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.1',
    description='Vent4US ventilator data processing.',
    url='https://github.com/vent4us/vent-plotting',
    author='Ethan Li',
    author_email='ethanli@stanfod.edu',
    packages=setuptools.find_packages(),
    install_requires=[
        'scipy',
        'numpy',
        'pandas',
        'coloredlogs',
        'matplotlib'
    ]
)
