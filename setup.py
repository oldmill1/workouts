#!/usr/bin/env python3
"""
Setup script for the Workouts CLI tool
"""

from setuptools import setup, find_packages

setup(
    name="workouts-cli",
    version="1.0.0",
    description="Vintage terminal-style workout data analyzer",
    long_description="A retro-styled command line tool for analyzing workout data with ASCII charts and spy-film aesthetics",
    author="Workout Data Analyst",
    python_requires=">=3.7",

    # Package configuration
    py_modules=["workouts"],

    # Dependencies
    install_requires=[
        "pandas>=1.3.0",
        "rich>=10.0.0",
    ],

    # Console script entry point
    entry_points={
        "console_scripts": [
            "workouts=workouts:main",
        ],
    },

    # Package metadata
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Utilities",
    ],

    # Additional files to include
    include_package_data=True,
)
