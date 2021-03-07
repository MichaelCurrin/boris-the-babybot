# Boris
> Tool to post daily random tweets for a responsible Twitter bot

[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/boris-the-babybot?include_prereleases&sort=semver)](https://github.com/MichaelCurrin/boris-the-babybot/releases/)
[![License - MIT](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Python - >=3.6](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![dependency - tweepy](https://img.shields.io/badge/dependency-tweepy-blue)](https://pypi.org/project/tweepy)


## Features

- Connect to the Twitter API.
- Tweet from the command-line or using a scheduled cron job.
- Generate a tweet message from your custom lists of messages, emojis and hashtags.
- Search for top tweets about a topic of interest and automatically favorite them.


## Example usage

After configuring auth details and setting up configured content, you can run [boris.py](/boris/boris.py) script on the command-line. This will generate a random status using configured text files and then post it as a tweet to a Twitter account.

```bash
$ ./boris.py
Message:
'Boris is replacing all his internet passwords with passwords of at least 20 characters. #GDPR'

Updating timeline.
See the tweet at: https://twitter.com/boristhebabybot
```

The [unicron](https://github.com/MichaelCurrin/unicron/) repo is recommended for scheduling this project to ensure the bot posts daily as soon as it can, without posting multiple times in the day. Also, if it fails to post, it will retry later.


## Who is Boris?

This project was developed to tweet random messages daily for the [Boris The BabyBot](https://twitter.com/boristhebabybot) account.

Though, this project could be configured easily to tweet for any Twitter account that you have access to, whether your personal account or a dedicated bot account.


## Authorization

To access the Twitter API, you must apply for a **Twitter developer account** - that takes time and effort.

You can copy the API credentials from your dev account to this project's local config on machine. See setup instructions in [Documentation](#documentation) for more details.


## Documentation

<div align="center">
  
[![view - Documentation](https://img.shields.io/badge/view-Project-documentation-blue?style=for-the-badge)](/docs/)

</div>


## Development

If you are interested in how this project works, see the [boris/lib/twitter.py](https://github.com/MichaelCurrin/boris-the-babybot/blob/master/boris/lib/twitter.py) module. That includes functions to connect and post to the Twitter API. It also combines the configured messages, emojis and hashtags randomly to generate a status.


## Am I allowed to make a bot?

You _are_ allowed by Twitter to make a bot account, but one that follows Twitter's restrictions.

I cover this in more details in the [Bots](https://michaelcurrin.github.io/python-twitter-guide/#/policies?id=bots) section of my Python Twitter Guide project.


## License

Released under [MIT](/LICENSE).
