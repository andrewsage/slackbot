SlackBot
----
Python based Slack Bot that makes use of `Python SlackClient`_

The inspiration
----

Using `How to Build Your First Slack Bot with Python`_, I went from not knowing Python to having my first bot up and running in under an hour. Using that knowledge as a basis I managed to put this together in under a day.



The following instructions are as much a reminder to myself how I did this as they are a guide to others.

Installation
----

SlackBot is available through the Python Package Index, PyPI_, you can install it with::

    pip install codethecity-slackbot

Alternatively, clone or fork the repository and use::

    python setup.py develop

to install locally for development. For local development you should also install the development dependencies (ideally in a ``virtualenv``) using::

    pip install -r requirements.txt

Usage
----

SlackBot
----
SlackBot is the base class that connects to your registered Slack Bot.

In order to use the class you must be using the your token from Slack. To set the environmant variable use::

    export SLACK_BOT_TOKEN='token'

It handles the following default commands:

* help - lists all other commands it provides
* who created - details of the author
* show selfied - shows an image of the bot
* show mugshot - shows a mugshot of the bot

EventbriteBot
----

EventbriteBot is a subclass of SlackBot and provides basic querying of Eventbrite events for a given user account.

It uses `Eventbrite Python SDK`_.

In order to use the class you must be using the your token from Eventbrite. To set the environmant variable use::

  export EVENTBRITE_TOKEN='token'

This is an example showing how the SlackBot class is subclassed and used.

Creating a sample project with SlackBot
----

Setup the working environment
----

Create a virtual Python environment::

  mkdir <botname>
  cd <botname>
  virtualenv venv

Start the virtual Python environemnt::

  source venv/bin/activate

Examples
----

See the /examples directory for examples of the kinds of bots that you can build with SlackBot.

Currently there is a bot for querying Eventbrite.

.. _PyPI: https://pypi.python.org/pypi
.. _`How to Build Your First Slack Bot with Python`: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
.. _`Python SlackClient`: http://slackapi.github.io/python-slackclient/
.. _`Eventbrite Python SDK`: http://eventbrite-sdk-python.readthedocs.io/en/latest/
