# Installation


## Setup a Python 3 virtual environment

Follow instructions in this [gist](https://gist.github.com/MichaelCurrin/3a4d14ba1763b4d6a1884f56a01412b7).


You can now continue to the [Usage](/docs/usage.md) doc.


## Configuration


```bash
$ cd boris/etc
```

Setup config file.

```bash
$ cp config.tmpl.yml config.local.yml
```

Create Tweet messaging content.

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
