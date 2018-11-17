# Project ASTA

10/10 best discord bot

## Getting Started

To add this bot to your Discord server, use [this](https://discordapp.com/oauth2/authorize?client_id=513198240922075137&scope=bot&permissions=8) link.

## Developing Project ASTA

In order to get started with Project ASTA you will need a couple of programs and files.

1. [GitHub Desktop](https://desktop.github.com/), in order to clone the repo and commit your changes you will need GitHub Desktop, it essentially is just a git client.

2. [Python 3.6.6](https://www.python.org/downloads/release/python-366/), Python 3.7 is not supported by discord.py and PyNaCl so using Python 3.6.6 is required.

3. discord.py, to install discord.py, use `python -m pip install -U discord.py[voice]` or `python3 -m pip install -U discord.py[voice]
` in a terminal.
4. Using GitHub Desktop, clone the repo.

5. Create config.json, in the same folder as the repo create a file named config.json that contains
```
{
    "token" : "and the token that you got in the Developer Portal here"
}
```

At this point you should be able to start the bot up and test it out.