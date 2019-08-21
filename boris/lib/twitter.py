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

    rand_status = random.choice(messaging['statuses'])

    if random.random() > 0.5:
        rand_hashtag = random.choice(messaging['hashtags'])
        msg = " ".join((rand_status, rand_hashtag))
    else:
        msg = rand_status

    return msg


def _update_status(msg):
    print("Tweet message:")
    print(repr(msg))

    # TODO: Use class for context and reuse?
    api = get_api_connection(**CONF['twitter_credentials'])

    status = api.update_status(msg)
    # TODO From config
    print("See the tweet at: https://twitter.com/boristhebabybot")

    return status


def tweet(msg=None):
    if not msg:
        msg = make_msg()

    return _update_status(msg)


if __name__ == '__main__':
    print(make_msg())
