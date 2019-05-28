from setuptools import setup, Distribution


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True


setup(
    name='lab08',
    version='0.1',
    packages=['permutations'],
    package_data={'permutations': ['permutations.dll']},
    distclass=BinaryDistribution,
    description='Python+C++',
    url='https://github.com/MatMark/',
    author='Mateusz Markowski',
    author_email='235605@student.pwr.edu.pl'
)