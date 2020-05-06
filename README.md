# Boris the BabyBot
> Automation tool to run a simple Twitter bot

## Features

- Connect to Twitter API.
- Tweet from the command-line or with a cronjob.
- Generate tweet message from your custom lists of messages, emojis and hashtags.
- Search for top tweets about a topic of interest and automatically favorite them.
- Built with Python3 and [tweepy](https://www.tweepy.org/).


## Example usage

After configuring auth details and setting up configured content, you can run [boris/boris.py](/boris/boris.py) script on the command-line. This will generate a random sttatus using configured text files and then post it as a tweet to a Twitter account.

```bash
$ ./boris.py
Message:
'Boris is replacing all his internet passwords with passwords of at least 20 characters. #GDPR'

Updating timeline.
See the tweet at: https://twitter.com/boristhebabybot
```


## Who is Boris?

This project was developed to tweet random messages daily for the [Boris The BabyBot](https://twitter.com/boristhebabybot) account.

Though, this project could be configured easily to tweet for any Twitter account that you have access to, whether your personal accoun or a decidated bot account.


## Authorization

To access the Twitter API, you must apply for a **Twitter developer account** - that takes time and effort. 

You can copy the API credentials from your dev account to this project's local config on machine. See setup instructions in [Documentation](#documentation) for more details.


## Documentation

- [Installation](/docs/installation.md)
- [Usage](/docs/usage.md)


## Development

If you are interested in how this project works, see the [boris/lib/twitter.py](https://github.com/MichaelCurrin/boris-the-babybot/blob/master/boris/lib/twitter.py) module. That includes functions to connect and post to the Twitter API. It also combines the configured messages, emojis and hashtags randomly to generate a status.


## Am I allowed to make a bot?

You _are_ allowed by Twitter to make a bot account, but one that follows Twitter's restrictions.

I cover this in more details in the [Bots](https://michaelcurrin.github.io/python-twitter-guide/#/policies?id=bots) section of my Python Twitter Guide project.
