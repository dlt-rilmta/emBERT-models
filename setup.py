#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from setuptools import find_namespace_packages, setup
from importlib import import_module


def readme():
    with open('README.md') as f:
        return f.read()


def read_model_name():
    # Place a file next to setup.py called model_name.txt containing only one one line which is the model name
    with open('model_name.txt') as f:
        return f.readline().strip()


model_name = read_model_name()
package_name = 'embert.models.' + model_name
model_version = import_module(package_name, model_name).__version__
# Create MANIFEST.in on-the-fly
with open('MANIFEST.in', 'w') as f:
    f.write('graft embert/models/' + model_name)

setup(name='embert-models-' + model_name.replace('_', '-'),
      packages=find_namespace_packages(include=[package_name]),
      include_package_data=True,
      version=model_version,
      description='A Python package for a model of the emBERT package called ' + model_name,
      long_description=readme(),
      url='https://github.com/dlt-rilmta/emBERT-models',
      author='Dávid Márk Nemeskey',
      license='LGPL v3.0',
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 5 - Stable',

          # Indicate who your project is intended for
          'Intended Audience :: Science/Research',
          # This one is not in the list...
          'Topic :: Scientific/Engineering :: Natural Language Processing',

          # Environment
          'Operating System :: POSIX :: Linux',
          'Environment :: Console',
          'Natural Language :: Hungarian',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
      ],
      keywords='BERT transformer NER chunking',
      # zip_safe=False,
      use_2to3=False)
