"""Packaging settings."""

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

#from pytip import __version__

# uses README.rst for documentation.
# Legitimate looking documentation when deploying to PyPI
this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

# running python setup.py test command
# entire package will be tested (assuming tests exist)
class RunTests(Command):
    """Run all tests."""

    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all test!"""
        errno = call(['py.test', '--cov=pytip', '--cov-report=term_missing'])
        raise SystemExit(errno)


setup(
    name = 'pytip',
    version = __version__,
    description = 'A tip calculator CLI program in Python.',
    long_description = long_description,
    url = 'https://github.com/chipsandtea/pytip',
    author = 'Christopher Hsiao',
    author_email = 'hsiao.christopher@gmail.com',
    license = 'MIT',
    classifiers = [
        'Intended Audience :: Users',
        'Topic :: Utilities',
        'License :: MIT',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'cli',
    # prevents installation of documentation or tests on a user's system!
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test' : ['coverage', 'pytest', 'pytest_cov'],
    },
    entry_points = {
        'console_scripts':[
            'pytip=pytip.cli:main',
        ],
    },
    cmdclass = {'test':RunTests},

)