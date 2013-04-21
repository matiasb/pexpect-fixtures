# Copyright (C) 2012  Matias Bordese
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


import sys

import pexpect

from pexpect_fixtures.instructions import (
    BREAKPOINT,
    COMMENT,
    EXPECT,
    SEND,
    MSG,
    INSTR_PATTERN,
)


class ExpectOpError(Exception):
    """Unexpected output error."""


def _expect_error(fixture, index):
    instructions = fixture[index:index + 2]
    msg = "expected '%s' not found" % instructions[0][1]
    if len(instructions) == 2 and instructions[1][0] == MSG:
        msg = instructions[1][1]
    raise ExpectOpError(msg)


def run(command, fixture, timeout=2, verbose=0):
    """Run command according to fixture."""
    child = pexpect.spawn(command)
    child.setecho(False)

    if verbose >= 2:
        child.logfile = sys.stdout

    for i, instr in enumerate(fixture):
        op, value = instr
        if op == EXPECT:
            expected = [pexpect.TIMEOUT, pexpect.EOF,
                        value.encode('string-escape')]
            res = child.expect(expected, timeout=timeout)
            if res in [0, 1]:
                _expect_error(fixture, i)
        elif op == SEND:
            child.sendline(value)
        elif op == BREAKPOINT:
            sys.stdout.write('-- Escape character is \'^]\'\n')
            child.interact()
        elif op == COMMENT and verbose >= 1:
            sys.stdout.write('-- %s\n' % value)
    return child
