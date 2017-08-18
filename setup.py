#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The setup script."""

from setuptools import setup

setup(
    name='sprint_names',
    version='1.0.0',
    url='https://github.com/dimaspivak/sprint_names',
    license='Apache Software License 2.0',
    author='Dima Spivak',
    author_email='dima@spivak.ch',
    description='Give your next sprint a cool name',
    py_modules=['sprint_names'],
    zip_safe=False,
    entry_points={'console_scripts': ['sprint_names = sprint_names:main']},
    include_package_data=True,
)
