# Boris the BabyBot
> Create and post tweets using the Twitter API.

This project could be modified easily to post for bot accounts but has been developed to tweet as the [Boris The BabyBot](https://twitter.com/boristhebabybot) Twitter account.


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

You do need a Twitter developer account and API credentials in order to use this tool. This step is covered in the installation doc.

- [Installation](/docs/installation.md)
- [Usage](/docs/usage.md)


## Am I allowed to make a bot?

You _are_ allowed by Twitter to make a bot account, but one that follows Twitter's restrictions.

Your bot can do things like tweet on a schedule, retweet other tweets (selectively but not in bulk) or repost external data or links such as blog posts. But you cannot message users, if they have not explicitly given permission (such as by messaging your account or opting in within a website/app).
