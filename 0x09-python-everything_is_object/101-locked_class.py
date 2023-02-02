#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """Prevent users from instantiating new
    LockedClass attributes apart
    from "first_name"
    """

    __slots__ = ["first_name"]
