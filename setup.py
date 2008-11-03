import sys
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='nose-all-modules',
    version='0.0.1',
    #author: Peter Fein  
    license = 'GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1',
    py_modules = ['allmodules'],
    entry_points = {
        'nose.plugins.0.10': [
            'allmodules = allmodules:AllModules'
            ]
        }
    )
