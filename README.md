# SlackBot
Python based Slack Bot that makes use of SlackClient

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
In order to use the class you must be using the your token from Eventbrite. To set the environmant variable use:

```
  export EVENTBRITE_TOKEN='token'
```

This is an example showing how the SlackBot class is subclassed and used.
