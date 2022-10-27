from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='micropython-stepmaker',
version='0.0.1',
description='Stepmaker Package For Stepmaker Kit Users and Rpi Pico Users. It is not an official Micropython package',
long_description=long_description,
long_description_content_type='text/markdown',
author='HwangJungeon',
author_email='hje@takeup.cc',
license='CC BY-NC-SA 4.0',
keywords=['stepmaker', 'step', 'maker', 'micropython'],
packages=['stepmaker']
)