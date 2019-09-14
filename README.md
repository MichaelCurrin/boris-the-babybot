# Boris the BabyBot
> Create and post tweets using the Twitter API

This project could be modified easily to post for bot accounts but has been developed to tweet as the [Boris The BabyBoy](https://twitter.com/boristhebabybot) Twitter account.

## Example Usage

Create a random message using configured text files and post to twitter using configured tokens.

```bash
$ ./boris.py
Message:
'Boris is replacing all his internet passwords with passwords of at least 20 characters. #GDPR'

Updating timeline.
See the tweet at: https://twitter.com/boristhebabybot
```

## Twitter bots

Note that you need to apply for a developer account on Twitter, with a motivation on how you will use the account. This can take a few days and a few emails to Twitter if you are not approved immediately.

You _are_ allowed by Twitter to make a bot account but with restrictions. It can do things like tweet on a schedule, retweet other tweets (selectively but not in bulk) or repost external data or links such as blog posts. But you cannot message users, if they have not explicitly given permission (such as by messaging your account or opting in within a website/app).

See the [Getting Started](https://developer.twitter.com/en/docs/basics/getting-started) guide on Twitter's developer docs.


## Documentation

- [Installation](/docs/installation.md)
- [Usage](/docs/usage.md)
