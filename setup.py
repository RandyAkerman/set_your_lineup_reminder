#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Randy Akerman",
    author_email='randy@akerman.org',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Create custom reminders to set your fantasy baseball line-up based on the schedule of a given day",
    entry_points={
        'console_scripts': [
            'set_your_lineup_reminder=set_your_lineup_reminder.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='set_your_lineup_reminder',
    name='set_your_lineup_reminder',
    packages=find_packages(include=['set_your_lineup_reminder', 'set_your_lineup_reminder.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/RandyAkerman/set_your_lineup_reminder',
    version='0.0.1',
    zip_safe=False,
)
