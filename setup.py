import sys
from pathlib import Path
from setuptools import setup
from setuptools.command.test import test as TestCommand


README = Path(__file__).parent / 'README.rst'


class PyTest(TestCommand):

    user_options = [
        ('addopts=', None, 'Additional options to be passed verbatim to the '
         'pytest runner')
    ]
    fixed_arguments = ''

    def initialize_options(self):
        super().initialize_options()
        self.addopts = ''

    def run_tests(self):
        import shlex
        import pytest
        errno = pytest.main(
            shlex.split(self.addopts + ' ' + self.fixed_arguments)
        )
        sys.exit(errno)


class UnitTests(PyTest):
    fixed_arguments = 'tests'


class IntegrationTests(PyTest):
    fixed_arguments = 'it'


setup(
    name='pylivy',
    version='0.0.1',
    description='A Python client for Apache Livy',
    long_description=README.read_text(),
    packages=['pylivy'],
    url='https://github.com/saivarunr/pylivy',
    author='Sai Varun Reddy Daram',
    author_email='saivarunvishal@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    setup_requires=[
        'wheel'
    ],
    cmdclass={
        'test': UnitTests,
        'it': IntegrationTests
    },
    install_requires=[
        'requests',
        'pandas'
    ],
    tests_require=[
        'pytest',
        'pytest-mock',
        'flask'
    ]
)
