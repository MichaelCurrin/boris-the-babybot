"""
Twitter library module.

The most important logic here connecting to and posting to the Twitter API.
"""
import random

import tweepy

from . import load_conf

CONF = load_conf()


def get_api_connection(
    consumer_key, consumer_secret, access_key=None, access_secret=None
):
    """
    Authenticate with Twitter API and return a connection object.

    If Access credentials are provided, create an App Access Token.
    Otherwise, create an Application-only Access Token, which has limited
    context but different API rate limit restrictions.
    See https://developer.twitter.com/en/docs/basics/authentication/overview/application-only
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    if access_key and access_secret:
        auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api


def make_msg():
    """
    Choose randomly to generate a message which includes emojis and hashtags.
    """
    messaging = CONF["messaging"]

    status = random.choice(messaging["statuses"])

    # For sales pitch tweets, don't use add-on pieces.
    if CONF["website"] in status:
        msg = status
    else:
        msg_pieces = [status]

        if random.random() > 0.5:
            emoji = random.choice(messaging["emojis"])
            msg_pieces.append(emoji)
        if random.random() > 0.5:
            hashtag = random.choice(messaging["hashtags"])
            msg_pieces.append(hashtag)

        msg = " ".join(msg_pieces)

    return msg.strip()


def show_statuses():
    """
    Print configured available status messages to choose from.

    Note based on printing of statuses - some emojis seem to have a backspace
    character builtin so the following character will be hidden unless there is
    a space between them. This only seems to be an issue in the console - when
    copying the console text to Twitter status box then it expands again.
    Some characters like 🇧🇼 show as block characters in the terminal.
    """
    messaging = CONF["messaging"]

    for status in messaging["statuses"]:
        print(status)
        print(repr(status))
        print()


def show_emojis():
    """
    Print configured available emojis to choose from.
    """
    messaging = CONF["messaging"]
    for emoji in messaging["emojis"]:
        print(emoji)
        print(repr(emoji))
        print()


def _update_status(msg):
    """
    Post given message as tweet or "status" on the Twitter user's profile.

    This is the core logic of this project.
    """
    # TODO: Use class with context for reuse.
    api = get_api_connection(**CONF["twitter_credentials"])

    status = api.update_status(msg)
    # TODO From config
    print("See the tweet at: https://twitter.com/boristhebabybot")

    return status


def tweet(msg=None, dry_run=False):
    """
    Post given message or generate a message and post it to the Twitter user's profile.
    """
    if not msg:
        msg = make_msg()
    print("Message: ")
    print(repr(msg))
    print()

    if dry_run:
        print("Skipping tweet step.")
    else:
        print("Updating timeline.")
        _update_status(msg)

    return msg


if __name__ == "__main__":
    print(make_msg())
