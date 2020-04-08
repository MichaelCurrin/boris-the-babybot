#!/usr/bin/env python
"""
Main application file.
"""
import argparse
import sys

import lib.twitter


def main(args):
    """
    Main command-line function.
    """
    parser = argparse.ArgumentParser(
        description="Boris the Twitterbot tweet tool. Default behavior is to"
        " create a random message using configured phrases, hashtags"
        " and emojis and then post the message to the configured Twitter"
        " account's timeline."
    )

    parser.add_argument(
        "-d", "--dry-run", action="store_true", help="Print message then exit.",
    )
    parser.add_argument(
        "-m",
        "--message",
        help="Use custom message. If flag is omitted, a random message will be used.",
    )
    parser.add_argument(
        "-e",
        "--emojis",
        action="store_true",
        help="Preview all configured emojis, as printed and store values, then exit.",
    )
    parser.add_argument(
        "-s",
        "--statuses",
        action="store_true",
        help="Preview all configured statuses, as printed and store values, then exit.",
    )

    args = parser.parse_args()

    if args.emojis:
        lib.twitter.show_emojis()
    elif args.statuses:
        lib.twitter.show_statuses()
    else:
        lib.twitter.tweet(args.message, args.dry_run)


if __name__ == "__main__":
    main(sys.argv[1:])
