import os


from setuptools import setup


setup(
    packages=['hathi_validate'],
    package_data={'hathi_validate':["xsd/*.xsd"]},
    test_suite="tests",
    setup_requires=['pytest-runner'],
    install_requires=["lxml", "PyYAML"],
    tests_require=['pytest'],

    entry_points={
                 'console_scripts': ['hathivalidate=hathi_validate.cli:main']
             },
)
