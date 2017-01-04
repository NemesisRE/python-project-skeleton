from setuptools import setup, find_packages
from subprocess import check_output
import sys, os, shlex

GIT_HEAD_REV = check_output(shlex.split('git rev-parse --short HEAD')).strip()

version = '0.1'

setup(name='NAME',
      version=version,
      description="This is my python project egg skeleton",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Steven "NemesisRE" Koeberich',
      author_email='nemesissre@gmail.com',
      url='https://nrecom.net',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      options = dict(egg_info = dict(tag_build = "dev_" + GIT_HEAD_REV)),
      )
