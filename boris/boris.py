#!/usr/bin/env python
"""
Main application file.
"""
import os
import sys

import lib.twitter


def main(args):
    """
    Main command-line function.
    """
    if set(args) & {'-h', '--help'}:
        name = os.path.basename(__file__)
        print(f"Usage: ./{name} [MESSAGE] [-h]", file=sys.stderr)
        return None

    if args:
        msg = args[0]
    else:
        msg = None
    lib.twitter.tweet(msg)


if __name__ == '__main__':
    main(sys.argv[1:])
