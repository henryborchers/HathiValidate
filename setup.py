from setuptools import setup

setup(
    name='HathiValidate',
    version='0.0.1',
    packages=['hathi_validate'],
    url='http://www.library.illinois.edu/dccdocs/hathi_validate/',
    license='University of Illinois/NCSA Open Source License',
    test_suite="tests",
    setup_requires=['pytest-runner'],
    install_requires=["lxml", "PyYAML"],
    tests_require=['pytest'],
    author='University of Illinois at Urbana Champaign',
    author_email='hborcher@illinois.edu',
    description='Replacement for older scripts for validating Hathi Trust Packages'
)
