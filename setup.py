import os


from setuptools import setup

metadata_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'hathi_validate', '__version__.py')
metadata = dict()
with open(metadata_file, 'r', encoding='utf-8') as f:
    exec(f.read(), metadata)

with open('README.rst', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()


setup(
    name=metadata['__title__'],
    version=metadata['__version__'],
    packages=['hathi_validate'],
    url=metadata['__url__'],
    license='University of Illinois/NCSA Open Source License',
    test_suite="tests",
    setup_requires=['pytest-runner'],
    install_requires=["lxml", "PyYAML"],
    tests_require=['pytest'],
    author=metadata['__author__'],
    author_email=metadata['__author_email__'],
    description=metadata['__description__'],
    entry_points={
                 'console_scripts': ['hathivalidate=hathi_validate.cli:main']
             },
)
