import os
import time
import re
from slackclient import SlackClient

class SlackBot(object):
  """
    A class for connecting a Bot to Slack.

    It provides basic functionality that can be expanded and modified
    via creating a subclass
  """
  # constants
  HELP_COMMAND = "help"
  SHOW_COMMAND = "show"
  WHO_COMMAND = "who"

  def __init__(self, name):
    """
      name - name of the bot as registered with Slack
    """

    self.name = name

    # instantiate Slack & Twilio clients
    self.slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    # Get the Bot's Slack ID
    api_call = self.slack_client.api_call("users.list")
    if api_call.get('ok'):
      # retrieve all users so we can find our bot
      users = api_call.get('members')
      for user in users:
        if 'name' in user and user.get('name') == self.name:
          self.bot_id = user.get('id')
          print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
      print("could not find bot user with the name " + self.name)

  def handle_help(self, commands):
    """
      Process the help command
    """
    # Place holder for any attachments we want to send
    attachments = []
    response = "I'm just a collection of 1s and 0s so the famous phrase 'garbage in, garbage out' applies to me.\n So far I've evolved to understand\n"

    # Add help message for each command
    response += "*" + self.HELP_COMMAND + "* - shows this message\n"
    response += "*" + self.SHOW_COMMAND + " selfie* - shows you what I look like\n"
    response += "*" + self.SHOW_COMMAND + " mugshot* - shows you what I look like\n"
    response += "*" + self.WHO_COMMAND + " created* - tells you about my creator\n"

    return response, attachments

  def handle_show(self, commands):
    """
      Process the show command
    """
    # Place holder for any attachments we want to send
    attachments = []
    response = ""
    if commands[1] == "selfie":
      image_url = "http://www.outofstorage.info/images/bot256.png"
      attachments = attachments = [{"title": "CareBot",
                            "image_url": image_url}]

    if commands[1] == "mugshot":
      image_url = "http://www.outofstorage.info/images/mug.jpg"
      attachments = attachments = [{"title": "CareBot mugshot",
                            "image_url": image_url}]

    return response, attachments

  def handle_who(self, commands):
    """
      Process the who command
    """
    # Place holder for any attachments we want to send
    attachments = []
    response = ""
    if commands[1] == "created":
      response = "I was created by Andrew Sage @symboticaandrew"

    return response, attachments

  def handle_command(self, command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    # Split the command into its list of words
    commands = command.split()

    response, attachments = self.parse_commands(commands, channel)

    self.send_response(response, channel, attachments)

  def parse_commands(self, commands, channel):
    """
      Parses the comamand received from Slack.
      Calls individual handler for each command group
    """

    # Place holder for any attachments we want to send
    attachments = []
    # Default response
    response = "Not sure what you mean. Use the *" + self.HELP_COMMAND + "* command to find out how to interact with me."

    if commands[0] == self.HELP_COMMAND:
      response, attachments = self.handle_help(commands)

    if commands[0] == self.SHOW_COMMAND:
      response, attachments = self.handle_show(commands)

    if commands[0] == self.WHO_COMMAND:
      response, attachments = self.handle_who(commands)

    return response, attachments

  def send_response(self, response, channel, attachments):
    """
      Sends the response to Slack.
    """
    self.slack_client.api_call("chat.postMessage", channel=channel,
                            text=response, as_user=True, attachments=attachments)

  def parse_slack_output(self, slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and "<@" + self.bot_id + ">" in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split("<@" + self.bot_id + ">")[1].strip().lower(), \
                       output['channel']
    return None, None

  def run(self):
    """
      Starts the Slack Bot running.
    """

    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if self.slack_client.rtm_connect():
        print(self.name + " connected and running!")
        while True:
            command, channel = self.parse_slack_output(self.slack_client.rtm_read())
            if command and channel:
                self.handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")