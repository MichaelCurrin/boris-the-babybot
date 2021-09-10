
# Configuration


```bash
$ cd boris/etc
```

## Set up config file.

Create a local config. This will not versioned and it should not be shared with anyone.

```bash
$ cp config.template.yml config.local.yml
```

In the local file, replace the placeholder API credentials with your own, from your Twitter developer account's app.


## Create Tweet messaging content

```bash
$ touch statuses.txt hashtags.txt emojis.txt
```

Add one or more lines to statuses so you have a sentence to tweet. You can use `\n` to represent a newline.

- _statuses.txt_
    ```
    This tweet was created by a bot.
    I like using the Twitter API.\n\nThanks Twitter!
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
