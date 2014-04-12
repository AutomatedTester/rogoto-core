import os
from setuptools import setup, find_packages

version = '0.2'

# get documentation from the README
try:
    here = os.path.dirname(os.path.abspath(__file__))
    description = file(os.path.join(here, 'README.md')).read()
except (OSError, IOError):
    description = ''

# dependencies
deps = []

setup(name='rogoto-core',
      version=version,
      description="Rogoto Core library that drives the BrickPI",
      long_description=description,
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: POSIX :: Linux'],
      keywords='brickpi',
      author='David Burns',
      author_email='david.burns@theautomatedtester.co.uk',
      url='https://github.com/AutomatedTester/rogoto-core',
      license='Apache',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=deps,
      )
