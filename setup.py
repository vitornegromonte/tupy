from setuptools import setup, find_packages

setup(
  name = 'Tupy',
  version = '0.0.1',
  packages=find_packages(where='src'),
  package_dir={'': 'src'},
  install_requires = [
    'numpy',
    'torch',
  ],
  entry_points = {
    'console_scripts': [
      'tupy = tupy.__main__:main'
    ]
  }
)