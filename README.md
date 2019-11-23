# Boris the BabyBot
> Automation tool to run a simple Twitter bot

- Twitter API.
- Tweet from the command-line or with a cronjob.
- Generate tweet message from your custom lists of messages, emojis and hashtags.

This project could be modified easily to post for any given Twitter bot, thought this has been developed specifically to tweet as [Boris The BabyBot](https://twitter.com/boristhebabybot).

## Example Usage

Create a random message using configured text files and post to twitter using configured tokens.

```bash
$ ./boris.py
Message:
'Boris is replacing all his internet passwords with passwords of at least 20 characters. #GDPR'

Updating timeline.
See the tweet at: https://twitter.com/boristhebabybot
```

## Documentation

To access the Twitter API through a script, you must apply for **Twitter developer account** and then copy API credentials from there to this project's config. See installation doc for more details

- [Installation](/docs/installation.md)
- [Usage](/docs/usage.md)


## Am I allowed to make a bot?

You _are_ allowed by Twitter to make a bot account, but one that follows Twitter's restrictions.

Your bot can do things like tweet on a schedule, retweet other tweets (selectively but not in bulk) or repost external data or links such as blog posts. But you cannot use your bot to create tweets to users or reply to users, unless the users have explicitly given permission (such as by messaging your account or opting in within a website/app).

If you do want to message other users, you can of course use your Twitter bot account in the browser without using the API.
