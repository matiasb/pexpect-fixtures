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

import os
import re

from pexpect_fixtures.instructions import (
    BREAKPOINT,
    COMMENT,
    EXPECT,
    SEND,
    MSG,
    INSTR_PATTERN,
)


class InvalidFixtureError(Exception):
    """Invalid fixture error."""


def load_fixture(filename):
    """Load a fixture file to memory."""
    instructions = []
    if os.path.exists(filename):
        with open(filename, 'r') as fixture_file:
            data = fixture_file.readlines()
            for i, line in enumerate(data, 1):
                line = line.strip()
                if line == '':
                    continue
                match = INSTR_PATTERN.match(line)
                if match:
                    instructions.append(match.groups())
                else:
                    raise InvalidFixtureError(
                        'Invalid instruction, line %d' % i)
    return instructions
