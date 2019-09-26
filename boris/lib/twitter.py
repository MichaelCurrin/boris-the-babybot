"""
Twitter library module.
"""
import random

import tweepy

from . import load_conf


CONF = load_conf()


def get_api_connection(consumer_key, consumer_secret, access_key,
                       access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    return api


def make_msg():
    messaging = CONF['messaging']

    status = random.choice(messaging['statuses'])

    # For sales pitch tweets, don't use add-ons.
    if CONF['website'] in status:
        msg = status
    else:
        msg_pieces = [status]

        if random.random() > 0.5:
            emoji = random.choice(messaging['emojis'])
            msg_pieces.append(emoji)
        if random.random() > 0.5:
            hashtag = random.choice(messaging['hashtags'])
            msg_pieces.append(hashtag)

        msg = " ".join(msg_pieces)

    return msg.strip()

def show_statuses():
    """
    Note based on printing of statuses - some emojis seem to have a backspace
    character builtin so the following character will be hidden unless there is
    a space between them. This only seems to be an issue in the console - when
    copying the console text to Twitter status box then it expands again.
    Some characters like 🇧🇼 show as block characters in the terminal.
    """
    messaging = CONF['messaging']
    for s in messaging['statuses']:
        print(s)
        print(repr(s))
        print()


def show_emojis():
    messaging = CONF['messaging']
    for e in messaging['emojis']:
        print(e)
        print(repr(e))
        print()


def _update_status(msg):
    # TODO: Use class for context and reuse?
    api = get_api_connection(**CONF['twitter_credentials'])

    status = api.update_status(msg)
    # TODO From config
    print("See the tweet at: https://twitter.com/boristhebabybot")

    return status


def tweet(msg=None, dry_run=False):
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


if __name__ == '__main__':
    print(make_msg())
