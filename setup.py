# Copyright (C) 2013  Matias Bordese
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from setuptools import setup, find_packages

setup(
    name='pexpect-fixtures',
    version='0.1',
    packages=find_packages(),
    scripts=['bin/pexpect-fixture-runner'],
    license='GPL-3',
    long_description='Simple pexpect test fixtures.',
    install_requires=['pexpect >= 2.3'],
)
