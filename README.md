# SlackBot
Python based Slack Bot that makes use of [Python SlackClient](http://slackapi.github.io/python-slackclient/)

# SlackBot
SlackBot is the base class that connects to your registered Slack Bot.

In order to use the class you must be using the your token from Slack. To set the environmant variable use:

```
  export SLACK_BOT_TOKEN='token'
```

It handles the following default commands:

* help - lists all other commands it provides
* who created - details of the author
* show selfied - shows an image of the bot
* show mugshot - shows a mugshot of the bot

# EventbriteBot
EventbriteBot is a subclass of SlackBot and provides basic querying of Eventbrite events for a given user account.

It uses [Eventbrite Python SDK](http://eventbrite-sdk-python.readthedocs.io/en/latest/).

In order to use the class you must be using the your token from Eventbrite. To set the environmant variable use:

```
  export EVENTBRITE_TOKEN='token'
```

This is an example showing how the SlackBot class is subclassed and used.


# The inspiration

Using [How to Build Your First Slack Bot with Python](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html), I went from not knowing Python to having my first bot up and running in under an hour. Using that knowledge as a basis I managed to put this together in under a day.

The following instructions are as much a reminder to myself how I did this as they are a guide to others.

# Creating a sample project with SlackBot

## Setup the working environment

Create a virtual Python environment:

```
  virtualenv <botname>
```

Start the virtual Python environemnt:

```
  source <botname>/bin/activate
```

Install the Slack API helper library:

```
  pip install slackclient
```


