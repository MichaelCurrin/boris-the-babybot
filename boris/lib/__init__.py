"""
Library initialization module.
"""
import datetime
import json
import os

import tweepy

import yaml


APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
ETC_DIR = os.path.join(APP_DIR, "etc")
VAR_DIR = os.path.join(APP_DIR, "var")


def read_text(path):
    """
    Read a file and return cleaned rows of content as a list.
    """
    with open(path) as f_in:
        lines = f_in.read().splitlines()

    return [line.replace("\\n", "\n") for line in lines if line]


def load_conf():
    """
    Read config files and return dict of config data.
    """
    yaml_path = os.path.join(ETC_DIR, "config.local.yml")
    with open(yaml_path) as f_in:
        conf = yaml.safe_load(f_in)

    statuses = read_text(os.path.join(ETC_DIR, "statuses.txt"))
    hashtags = read_text(os.path.join(ETC_DIR, "hashtags.txt"))
    emojis = read_text(os.path.join(ETC_DIR, "emojis.txt"))

    conf["messaging"] = dict(statuses=statuses, hashtags=hashtags, emojis=emojis)
    conf["website"] = "https://boristhebabybot.org"

    return conf


def test():
    """
    Pretty print the config data.
    """
    conf = load_conf()
    print(json.dumps(conf, indent=4))


if __name__ == "__main__":
    test()
