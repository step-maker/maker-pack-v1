from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='micropython-makerpack',
version='0.1.0',
description='Package for maker kit and every other makers.',
long_description=long_description,
long_description_content_type='text/markdown',
author='step maker',
author_email='pack-dev@stepmaker.co',
license='CC BY-NC-SA 4.0',
keywords=['stepmaker', 'step', 'maker', 'micropython', 'makerpack', 'pack', 'takeup'],
packages=['makerpack']
)