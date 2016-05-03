#!/usr/bin/env python
from setuptools import setup
from requirements import r

setup(
    name='kaggledigit',
    version='0.0.1',
    **r.dependencies)