"""
Library initialization module.
"""
import datetime
import json
import tweepy
import os

import yaml


APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
ETC_DIR = os.path.join(APP_DIR, 'etc')
VAR_DIR = os.path.join(APP_DIR, 'var')


def read_text(path):
    """
    Read and clean text from a path to a text file.
    """
    with open(path) as f_in:
        lines = f_in.read().splitlines()

    return [line.replace("\\n", "\n") for line in lines if line]


def load_conf():
    """
    Read config files and return dict of config data.
    """
    yaml_path = os.path.join(ETC_DIR, 'config.local.yml')
    with open(yaml_path) as f_in:
        conf = yaml.load(f_in, Loader=yaml.Loader)

    statuses = read_text(os.path.join(ETC_DIR, 'statuses.txt'))
    hashtags = read_text(os.path.join(ETC_DIR, 'hashtags.txt'))

    conf['messaging'] = dict(
        statuses=statuses,
        hashtags=hashtags,
    )

    return conf


def test():
    """
    Pretty print the config data.
    """
    import json
    conf = load_conf()
    print(json.dumps(conf, indent=4))


if __name__ == '__main__':
    test()