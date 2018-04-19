# -*- coding: utf-8 -*-

"""
Copyright (C) 2018  Daniele Giudice
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# This import ensure py2.7 compatibility
from __future__ import print_function
improt sys

def print_sm(*args, **kwargs):
    # Print in the same line
    print(*args, end='', **kwargs)
    sys.stdout.flush()

def print_err(*args, **kwargs):
    # Print to stderr
    print(*args, file=sys.stderr, **kwargs)

def print_err_sm(*args, **kwargs):
    # Print to stderr in the same line
    print(*args, file=sys.stderr, end='', **kwargs)
    sys.stderr.flush()
