# Installation


## Setup a Python 3 virtual environment

Follow instructions in this [gist](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).


## Get a Twitter developer account


Without a developer account, you cannot create the app tokens that the Twitter API needs for authentication. These are needed whenever you do requests such as fetch or create Twitter content.

You need to apply for a developer account on Twitter, including a written a motivation on how you will use the account. This can take a few days and a few emails to Twitter if you are not approved immediately.

- [How to apply for a Twitter Developer account](https://www.extly.com/docs/autotweetng_joocial/tutorials/how-to-auto-post-from-joomla-to-twitter/apply-for-a-twitter-developer-account/#apply-for-a-developer-account) blog post
- [Getting Started](https://developer.twitter.com/en/docs/basics/getting-started) guide for using the Twitter API.
- [Apps](https://developer.twitter.com/en/apps) list page for your Twitter account


## Configuration


```bash
$ cd boris/etc
```

### Setup config file.

Create a local config. This will not versioned and it should not be shared with anyone.

```bash
$ cp config.tmpl.yml config.local.yml
```

In the local file, replace the placeholder API credentials with your own, from your Twitter developer account's app.


### Create Tweet messaging content


```bash
$ touch statuses.txt hashtags.txt emojis.txt
```

Add one or more lines to statuses so you have a sentence to tweet.

- _statuses.txt_
    ```
    This tweet was created by a bot.
    I like using the Twitter API.
    I tweet therefore I am.
    ```

Optionally add one or more lines to hashtags file and a emojis file. These will be added after the sentence, with random chance of a hashtag piece being added and a random chance of an emoji piece being added.

- _hashtags.txt_
    ```
    #tweepy
    #python
    #twitterapi #python
    ```
- _emojis.txt_
    ```
    🐯
    🐦
    🤖
    🎙️
    ```
