#!/usr/bin/env python
# (C) Copyright 2010 Brandyn A. White
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Example python script
Usage:
python base.py
"""

__author__ = 'Brandyn A. White <bwhite@cs.umd.edu>'
__version__ = '0.1'
__license__ = 'GPL V3'


def example_func(a, b):
    """Example function that divides numbers

    Args:
        a: Numerator (float)
        b: Denominator (float)

    Returns:
        a divided by b

    Raises:
        ZeroDivisionError: b is equal to zero.
    """
    return a / b


def example_gen(a):
    """Example generator of sums of sequential numbers starting at a

    Args:
        a: initial number

    Yields:
        The sum
    """
    s = a
    while 1:
        yield s
        a += 1
        s += a


def _main():
    print(__doc__)

if __name__ == '__main__':
    _main()
