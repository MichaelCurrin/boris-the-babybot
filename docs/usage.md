# Usage


```bash
$ cd <PATH_TO_REPO>
$ source venv/bin/activate
```

```bash
$ cd boris
```

## Help

```
$ ./boris.py --help
usage: boris.py [-h] [-d] [-m MESSAGE] [-e] [-s]

Boris the Twitterbot tweet tool. Default behavior is to create a random
message using configured phrases, hashtags and emojis and then post the
message to the configured Twitter account's timeline.

optional arguments:
  -h, --help            show this help message and exit
  -d, --dry-run         Print message then exit.
  -m MESSAGE, --message MESSAGE
                        Use custom message. If flag is omitted, a random
                        message will be used.
  -e, --emojis          Preview all configured emojis, as printed and store
                        values, then exit.
  -s, --statuses        Preview all configured statuses, as printed and store
                        values, then exit.
```

## Commands

```bash
$ ./boris
```

```bash
$ ./boris --dry-run
```

```bash
$ ./boris --message 'My custom tweet message'
```

```bash
$ ./boris --emojis
```

```bash
$ ./boris --statuses
```
