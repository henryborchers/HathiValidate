import hathi_validate

from setuptools import setup

setup(
    name=hathi_validate.__title__,
    version=hathi_validate.__version__,
    packages=['hathi_validate'],
    url=hathi_validate.__url__,
    license='University of Illinois/NCSA Open Source License',
    test_suite="tests",
    setup_requires=['pytest-runner'],
    install_requires=["lxml", "PyYAML"],
    tests_require=['pytest'],
    author=hathi_validate.__author__,
    author_email=hathi_validate.__author_email__,
    description=hathi_validate.__description__,
    entry_points={
                 'console_scripts': ['hathivalidate=hathi_validate.cli:main']
             },
)
