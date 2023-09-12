#!/usr/bin/python3
"""A rebel kind of int"""


class MyInt(int):
    """a rebel my int class"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
